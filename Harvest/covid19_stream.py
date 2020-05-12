import requests
import json
import time
import couchdb
from threading import Thread

consumer_key = ""
consumer_secret = ""

# AU coord
lat_range = [ -43.00311, -12.46113]
lng_range = [113.6594, 153.61194]
bounding_box = [
    [lat_range[0],lng_range[0]],
    [lat_range[1],lng_range[0]],
    [lat_range[0],lng_range[1]],
    [lat_range[1],lng_range[1]]
]

# auth
def get_bearer_token(key, secret):
    response = requests.post(
        "https://api.twitter.com/oauth2/token",
        auth=(key, secret),
        data={'grant_type': 'client_credentials'},
        headers={"User-Agent": "TwitterDevCovid19StreamQuickStartPython"})
    if response.status_code is not 200:
        raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" % (response.status_code, response.text))
    body = response.json()
    return body['access_token']

# database
table_tweet_name = 'tweet'
database_host = 'http://<host>/<schema>'
database_server = couchdb.Server(database_host)

# init db
if table_tweet_name in database_server:
    table_tweet = database_server[table_tweet_name]
else:
    table_tweet = database_server.create(table_tweet_name)

# counter
count={
    'total':0,
    'au': 0
}
# save data
def save_data(data):
    global file_object, count, file_name
    if file_object is None:
        count['total'] += 1
        return
    else:
        tweet_id = data['id']
        if tweet_id not in table_tweet:
            lat = None,
            lng = None,
            if 'coordinates' in data:
                lat = data['coordinates']['coordinates'][1]
                lng = data['coordinates']['coordinates'][0]
            if 'geo' in data:
                lat = data['coordinates']['coordinates'][0]
                lng = data['coordinates']['coordinates'][1]
            table_tweet[tweet_id] = {
                'raw': data,
                'lat': lat,
                'lng': lng
            }
            count['total'] += 1
            count['au'] += 1

# call api
def stream_connect(partition):
    response = requests.get("https://api.twitter.com/labs/1/tweets/stream/covid19?partition={}".format(partition),
                            headers={"User-Agent": "TwitterDevCovid19StreamQuickStartPython",
                                     "Authorization": "Bearer {}".format(
                                         get_bearer_token(consumer_key, consumer_secret))},
                            stream=True)
    for response_line in response.iter_lines():
        save_data(geo_filter(response_line))

# latlng in AU
def in_place(data):
    coord = data['geo']['coordinates'] # lat, lng
    return lat_range[0]<=coord[0]<=lat_range[1] and lng_range[0]<=coord[1]<=lng_range[1]

# return json data if in AU else None
def geo_filter(data):
    if 'coordinates' in data and (lat_range[0]<=data['coordinates']['coordinates'][1]<=lat_range[1] and lng_range[0]<=data['coordinates']['coordinates'][0]<=lng_range[1]):
        return json.loads(data)
    if 'geo' in data and (lat_range[0]<=data['geo']['coordinates'][0]<=lat_range[1] and lng_range[0]<=data['geo']['coordinates'][1]<=lng_range[1]):
        return json.loads(data)
    elif 'place' in data and data['place']['country_code'] == 'AU':
        return json.loads(data)
    else:
        return None
            
def main():
    timeout = 0
    start = time.perf_counter ()
    while True:
        for partition in range(1, 5):
            Thread(target=stream_connect, args=(partition,)).start()
        time.sleep(2 ** timeout * 1000)
        timeout += 1
        now = time.perf_counter ()
        used = now-start
        print('\r%ds, total: %d, au: %d'%(used, count['total'], count['au']))

if __name__ == "__main__":
    main()