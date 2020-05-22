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
    full_name = []
    coordinates = []
    ids = []
    lang = []
    geo = Nominatim()
    for item in db.view("_design/newDesign/_view/new-view"):
        tweet_id = item.value['id']
        if tweet_id not in ids:
            ids.append(tweet_id)
            longitude = 0
            latitude = 0
            for i in range(0,3):
                longitude += item.value['place']['bounding_box']['coordinates'][0][i][0]
                latitude += item.value['place']['bounding_box']['coordinates'][0][i][1]
            coordinates.append([longitude/4,latitude/4])
            full_name.append(item.value['place']['full_name'])
            lang.append(item.value['lang'])

    data = {'full_name': full_name, 'coordinates': coordinates}
    df = pd.DataFrame(data=data)
    city = pd.DataFrame({'content':full_name})['content'].str.split(',', expand=True)
    data_lang = {'city': city[0].values.tolist(), 'state': city[1].values.tolist(), 'coordinates': coordinates, 'lang': lang,'count':ids}
    dlf = pd.DataFrame(data=data_lang)
    city_lang = dlf.groupby(['city','lang']).count()
    clf = pd.DataFrame(city_lang)["count"].reset_index(name="Count")
    save_result(clf, "city_lang_results")
#city lang state count
    return df


def tweets_count(df):
    city_NumTweet = df.groupby(['full_name']).count()
    city_df = pd.DataFrame(city_NumTweet)["coordinates"].reset_index(name="Tweets_Num")
    full_name = city_df['full_name']
    city = full_name.str.split(',', expand=True)
    city_state = pd.DataFrame({'full_name': full_name, 'city': city[0].values.tolist(), 'state': city[1].values.tolist()})
    city_df = pd.merge(city_df, city_state, on='full_name')
    return city_df
# full_name city state Tweets_Num Hospital_Num

def data_combine(tweet_df, aurin_df):
    geolocator = Nominatim()
    latitude = aurin_df[' latitude'].values.tolist()
    longitude = aurin_df[' longitude'].values.tolist()
    state = aurin_df[' state'].values.tolist()
    for i in range(len(state)):
        state[i] = state_code[state[i]]

    coordinates = []
    city_list = tweet_df['city'].values.tolist()
    city_aurin = []
    for i in range(len(latitude)):
        hasCity = False
        city_name = geolocator.reverse(str(latitude[i]) + "," + str(longitude[i]))
        coordinates.append([longitude[i], latitude[i]])
        for j in range(len(city_list)):
            if city_list[j] in city_name.address:
                city_aurin.append(city_list[j])
                hasCity = True
                break

        if not hasCity:
            city_aurin.append('Unknown')

    full_name = []
    for i in range(city_aurin):
        full_name.append(city_aurin[i]+','+state[i])

    citys_hospital = pd.DataFrame({'full_name':full_name,'city': city_aurin, 'state': state, 'coordinate': coordinates})
    hospital_num = citys_hospital.groupby['city']
    new_aurin_df = pd.DataFrame(hospital_num)['coordinate'].reset_index(name="Hospital_Num")
    final_df = pd.merge(tweet_df, new_aurin_df, on='city')

    return final_df


def save_result(final_df, database_name):
    couch = couchdb.Server('http://admin:12345@127.0.0.1:5984//')

    if database_name in couch:
        del couch[database_name]
        couch = couch.create(database_name)
    else:
        couch = couch.create(database_name)

    final_json = final_df.to_json(orient="columns", force_ascii=False)
    couch.save(json.loads(final_json))


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

main()