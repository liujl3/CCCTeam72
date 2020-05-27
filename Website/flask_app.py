from flask import Flask
from flask import jsonify
from flask import send_from_directory
import couchdb
app = Flask(__name__,static_folder="./team-72-web/dist/static/")


database_name = "city_lang_results"
database_host = "http://admin:123456@45.113.235.44:5984/"
database_server = couchdb.Server(database_host)


state_6 = ["New South Wales", "Victoria", "Queensland",
           "Western Australia", "South Australia", "Tasmania"]
states = ["New South Wales", "Victoria", "Queensland", "Western Australia", "South Australia", "Tasmania",
          "Australian Capital Territory", "Northern Territory", "Jervis Bay Territory"]

# /timeline_data

lang_code = {"en": "English (en)", "ar": "Arabic (ar)", "bn": "Bengali (bn)",
             "cs": "Czech (cs)", "da": "Danish (da)", "de": "German (de)",
             "el": "Greek (el)", "es": "Spanish (es)", "fa": "Persian (fa)",
             "fi": "Finnish (fi)", "fil": "Filipino (fil)", "fr": "French (fr)",
             "he": "Hebrew (he)", "hi": "Hindi (hi)", "hu": "Hungarian (hu)",
             "id": "Indonesian (id)", "it": "Italian (it)", "ja": "Japanese (ja)",
             "ko": "Korean (ko)", "msa": "Malay (msa)", "nl": "Dutch (nl)",
             "no": "Norwegian (no)", "pl": "Polish (pl)", "pt": "Portuguese (pt)",
             "ro": "Romanian (ro)", "ru": "Russian (ru)", "sv": "Swedish (sv)",
             "th": "Thai (th)", "tr": "Turkish (tr)", "uk": "Ukrainian (uk)",
             "ur": "Urdu (ur)", "vi": "Vietnamese (vi)", "zh": "Chinese (zh)",
             "zh-cn": "Chinese(cn)", "zh-tw": "Chinese(cn)"}


def clear_timeline(db):
    result = {}
    axis_list = []
    for time in db["day"].values():
        if time not in axis_list:
            axis_list.append(time)
    axis_list.sort()

    data_piece = []

    for name in states:
        # initialise
        print(name)
        date_value = [0 for n in range(len(axis_list))]
        state_data = {"name": '', "type": "line", "data": date_value}

        state_data["name"] = name
        for index in db["state"].keys():

            state_name = db["state"][index]
            state_date = db["day"][index]
            tweets_num = db["Tweets_Num"][index]
            if name.strip() == state_name.strip():
                date_index = axis_list.index(state_date)
                state_data["data"][date_index] += tweets_num
        data_piece.append(state_data)

    date_list = []

    for item in axis_list:
        item = item[5:7] + '/' + item[8:]
        date_list.append(item)

    result["xAxis"] = date_list
    result["data"] = data_piece

    return result
# /city_data


def clear_city_old(city):
    state_6 = ["New South Wales", "Victoria", "Queensland",
               "Western Australia", "South Australia", "Tasmania"]
    result = {}
    state_sum = []
    city_sum = []
    for name in state_6:
        state_data = {"name": '', "value": 0}
        detail_data = {"cat": '', "data": ''}
        full_name = city["full_name"]
        check_city = []
        cities = []
        for index in full_name.keys():
            city_data = {"name": '', "value": 0}
            city_name = full_name[index].split(',')[0]
            # print(city_name)
            state_name = full_name[index].split(',')[1]
            tweets_num = city["Tweets_Num"][index]
            if name.strip() == state_name.strip():
                state_data["name"] = name
                state_data["value"] += tweets_num
                if city_name not in check_city:
                    check_city.append(city_name)
                    city_data["name"] = city_name
                    city_data["value"] += tweets_num
                else:
                    city_data["value"] += tweets_num
                cities.append(city_data)
        # sorted(detail_data["data"])
        detail_data["cat"] = name
        detail_data["data"] = cities
        city_sum.append(detail_data)
        state_sum.append(state_data)
    final_data = []
    state_final = {}
    state_final["cat"] = "Total"
    state_final["data"] = state_sum
    final_data.append(state_final)
    for item in city_sum:
        final_data.append(item)
    result["data"] = final_data

    return result


def clear_city(record):
    state_6 = ["New South Wales", "Victoria", "Queensland",
               "Western Australia", "South Australia", "Tasmania"]
    cities = record["city"]
    tweet_nums = record["Tweets_Num"]
    hospital_nums = record["Hospital_Num"]
    result = {"data": []}
    tweets_of_all = []
    hospitals_of_all = []
    for state in state_6:
        filtered_state_ids = [
            key for key in record["state"].keys() if record["state"][key].strip() == state.strip()]
        tweets_of_state = []
        hospitals_of_state = []
        tweet_counter = 0
        hospital_counter = 0
        for state_id in filtered_state_ids:
            city = cities[state_id]
            tweet_num = tweet_nums[state_id]
            hospital_num = hospital_nums[state_id]
            tweets_of_state.append({"name": city.strip(), "value": tweet_num})
            hospitals_of_state.append({"name": city.strip(), "value": hospital_num})
            tweet_counter += tweet_num
            hospital_counter += hospital_num
        tweets_of_all.append({"name": state.strip(), "value": tweet_counter})
        hospitals_of_all.append({"name": state.strip(), "value": hospital_counter})
        result["data"].append({
            "cat": state,
            "tweets": tweets_of_state,
            "hospitals": hospitals_of_state
        })
    result["data"].append({
        "cat": "Total",
        "tweets": tweets_of_all,
        "hospitals": hospitals_of_all
    })
    return result


# /lang_data
def clear_lang(db):

    temp_response = {
        "data": []
    }
    response = temp_response
    sum = {}
    for index in db['lang']:
        language = db['lang'][index]
        num = db['Count'][index]
        if language in sum.keys():
            sum[language] += num
        else:
            sum[language] = num

    other_lang = {'name': 'Unknown', 'value': 0}
    other = []
    for lang in sum.keys():
        tmp = {}
        if lang in lang_code.keys():

            tmp['name'] = lang_code[lang]
            tmp['value'] = sum[lang]
            print(tmp)
            response['data'].append(tmp)

        else:
            other_lang['value'] += sum[lang]

    response['data'].append(other_lang)
    return response

# /dot_data


def clear_dot(dot):
    result = {}
    tweets = []
    for index in dot["coordinate"].keys():
        tweet_data = {}
        coord = dot["coordinate"][index]
#         tweet_data["coordinate"] = coord
        tweets.append(coord)
    result["tweets"] = tweets
    return result


def read_dot(db_name, key):
    db_dot = database_server[db_name]
    data_dot = []
    for i in db_dot:
        data_dot = db_dot[i]
    result = []
    for index in data_dot[key].keys():
        coord = data_dot[key][index]
        result.append(coord)
    return result


@app.route('/', methods=['GET'])
def index():
     return send_from_directory("./team-72-web/dist/", "index.html")


@app.route('/home', methods=['GET'])
def home():
     return send_from_directory("./team-72-web/dist/", "index.html")


@app.route('/timeline_data', methods=['GET'])
def get_timeline():
    result_timeline = {}
    db_timeline = database_server["day_state_tweets"]

    for i in db_timeline:
        data_timeline = db_timeline[i]

    try:
        result_timeline = clear_timeline(data_timeline)
    except Exception as e:
        result_timeline['status'] = 'false'
        result_timeline['message'] = e
    else:
        result_timeline['status'] = 'true'
        result_timeline['message'] = 'None'

    return jsonify(result_timeline)


@app.route('/city_data', methods=['GET'])
def get_city():
    result_city = {}
    db_city = database_server["result"]

    for i in db_city:
        data_city = db_city[i]

    try:
        result_city = clear_city(data_city)
    except Exception as e:
        result_city['status'] = 'false'
        result_city['message'] = str(e)
    else:
        result_city['status'] = 'true'
        result_city['message'] = 'None'

    return jsonify(result_city)


@app.route('/lang_data', methods=['GET'])
def get_lang():
    db_lang = database_server["city_lang_results"]

    result_lang = {}
    for i in db_lang:
        data_lang = db_lang[i]
    #result = count_lang(data)
    try:
        result_lang = clear_lang(data_lang)
    except Exception as e:
        result_lang['status'] = 'false'
        result_lang['message'] = e
    else:
        result_lang['status'] = 'true'
        result_lang['message'] = 'None'

    return jsonify(result_lang)


@app.route('/dot_data', methods=['GET'])
def get_dot():
    # db_dot = database_server["tweet_coord"]

    result_dot = {}
    # for i in db_dot:
    #     data_dot = db_dot[i]

    try:
        result_dot["tweets"] = read_dot("tweet_coord", "coordinate")
        result_dot["hospitals"] = read_dot("hosp_coord", "coordinates")
        # result_dot = clear_dot(data_dot)
    except Exception as e:
        result_dot['status'] = 'false'
        result_dot['message'] = str(e)
    else:
        result_dot['status'] = 'true'
        result_dot['message'] = 'None'

    return jsonify(result_dot)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
