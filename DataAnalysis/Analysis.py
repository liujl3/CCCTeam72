import numpy
import pandas as pd
import couchdb
import json
from pprint import pprint
import sys
from geopy.geocoders import Nominatim
import requests

state_code = {'QLD': 'Queensland', 'NT': 'Northern Territory', 'WA': 'Western Australia', 'SA': 'South Australia',
              'NSW': 'New South Wales', 'VIC': 'Victoria', 'TAS': 'Tasmania', 'ACT': 'Australian Capital Territory'}


def connect_database(database_name):
    couch = couchdb.Server('http://admin:12345@127.0.0.1:5984//')
    db = couch[database_name]

    return db


def gather(db):
    city = []
    coordinates = []
    ids = []
    geo = Nominatim()
    for id in db:  # 这里应该有个mapreduce的视图
        content = db[id]
        if content['id'] not in ids:
            ids.append(content['id'])
            coordinates.append(content['bounding_box']['coordinates'])
            city.append(content["full_name"])

    d = {'full_name': city, 'coordinates': coordinates}
    df = pd.DataFrame(data=d)
    return df


def tweets_count(df):
    city_NumTweet = df.groupby(['full_name']).count()
    city_df = pd.DataFrame(city_NumTweet)["coordinates"].reset_index(name="Tweets_Num")
    full_name = city_df['full_name']
    city = full_name.str.split(',', expand=True)
    city_state = pd.DataFrame({'full_name': full_name, 'city': city.icol(0), 'state': city.icol(1)})
    city_df = pd.merge(city_df, city_df, on='full_name')
    return city_df


def data_combine(tweet_df, aurin_df):
    geolocator = Nominatim()
    latitude = aurin_df['latitude'].values.tolist()
    longitude = aurin_df['longitude'].values.tolist()
    citys_hospital = pd.DataFrame({'state': aurin_df['state'], 'coordinate': [longitude, latitude]})  # 对应不到市一级，名字不一样
    hospital_num = citys_hospital.groupby['state']
    new_aurin_df = pd.DataFrame(hospital_num)['coordinate'].reset_index(name="Hospital_Num")
    final_df = pd.merge(tweet_df, new_aurin_df, on='state')

    return final_df


def save_result(final_df, database_name):
    couch = couchdb.Server('http://admin:12345@127.0.0.1:5984//')

    if database_name in couch:
        del couch[database_name]
        couch = couch.create(database_name)
    else:
        couch = couch.create(database_name)

    final_json = final_df.to_json(orient="columns", force_ascii=False)
    couch.save(final_json)


def main():
    resource_database = 'tweet'
    result_database = 'result'
    db = connect_database(resource_database)
    tweet_df = gather(db)
    count_df = tweets_count(tweet_df)
    aurin_file = pd.read_csv('Hospital.csv')
    aurin_df = pd.DataFrame(aurin_file)
    final_df = data_combine(count_df, aurin_df)
    save_result(final_df, result_database)