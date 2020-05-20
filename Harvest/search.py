import sys
import requests
import json
import time
import couchdb
from threading import Thread

consumer_key = "MMgOYPM04mx1Hl5OB0SLbKWVK"
consumer_secret = "jWwc4amOZWEqCsm6MvAFRXDzGC7cxcngje1kobRe6sDnFJqvZe"

# AU coord
# lat_range_au = [ -12.46113, -43.00311 ]
# lng_range_au = [113.6594, 153.61194]
# bounding_box_au = [lng_range_au[0],lat_range_au[0],lng_range_au[1],lat_range_au[1]]

# time 2020/01/01 - 2020/05/01
# date = [str(d*1000000+10000) for d in range(202001, 202006)]
# dev
date = ["202004200000","202005200000"]

# auth


def get_bearer_token(key, secret):
    response = requests.post(
        "https://api.twitter.com/oauth2/token",
        auth=(key, secret),
        data={'grant_type': 'client_credentials'},
        # headers={"User-Agent": "TwitterDevCovid19StreamQuickStartPython"})
    )
    if response.status_code is not 200:
        raise Exception(f"Cannot get a Bearer token (HTTP %d): %s" %
                        (response.status_code, response.text))
    body = response.json()
    return body['access_token']

# database
database_name = "tweet"
database_host = "http://admin:123456@45.113.232.155:5984/"
database_server = couchdb.Server(database_host)
database_status_name = "status"
# init db
if database_name in database_server:
    database_tweet = database_server[database_name]
else:
    database_tweet = database_server.create(database_name)
if database_status_name in database_server:
    database_status = database_server[database_status_name]
else:
    database_status = database_server.create(database_status_name)

# save data
def save_tweet(tweet):
    tweet_id = tweet['id']
    if str(tweet_id) not in database_tweet:
        database_tweet[str(tweet_id)] = {
            'time': tweet['created_at'],
            'lang': tweet['lang'] if 'lang' in tweet else None,
            'raw': tweet
        }
        # additional tables
        # related_tweet - (tweet_id, related, date, state, lang)

# call api
def search_data(next, fromDate, toDate):
    try:
        # has:geo
        params = {
            "query": "place_country:AU has:geo",
            "fromDate": fromDate,
            "toDate": toDate,
            "maxResults": 500
        }
        if next:
            params["next"] = next
        response = requests.post("https://api.twitter.com/1.1/tweets/search/30day/ccc.json",
                                 headers={
                                     "content-type": "application/json",
                                     "authorization": "Bearer {}".format(
                                         get_bearer_token(consumer_key, consumer_secret))},
                                 json=params,
                                 stream=True)
        data = json.loads(response.content)
        for tweet in data['results']:
            save_tweet(tweet)
        if 'next' in data:
            return True, data['next'], None
        else:
            return True, None, None
    except Exception as e:
        return False, None, e

def record_status(partID, i, status, e, next, fromDate, toDate):
    database_status[str(i)+"-"+str(partID)] = {
        "status": status,
        "error": str(e),
        "dateIndex": i,
        "next": next,
        "fromDate": fromDate,
        "toDate": toDate
    }

def main(start_date_index, next):
    next = next if next else None
    partID = 0
    for i in range(start_date_index if start_date_index else 0, len(date)-1):
        fromDate = date[i]
        toDate = date[i+1]
        while True:
            status, next, e = search_data(next, fromDate, toDate)
            record_status(partID, i, status, e, next, fromDate, toDate)
            print(str(partID) + ":\t" + str(status))
            time.sleep(1)
            if next == None:
                break
            partID += 1

if __name__ == "__main__":
    main(sys.argv[0] if len(sys.argv) == 2 else None, sys.argv[1] if len(sys.argv) == 2 else None)
