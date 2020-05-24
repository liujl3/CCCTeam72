from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import couchdb
app = Flask(__name__)




database_name = "city_lang_results"
database_host = "http://admin:123456@45.113.235.44:80/"
database_server = couchdb.Server(database_host)
db = database_server["city_lang_results"]


temp_response ={
    "data":[]
    }

lang_code = {"en": "English (en)", "ar": "Arabic (ar)", "bn": "Bengali (bn)",
             "cs": "Czech (cs)","da": "Danish (da)","de": "German (de)", 
             "el": "Greek (el)", "es": "Spanish (es)", "fa": "Persian (fa)",
             "fi": "Finnish (fi)","fil": "Filipino (fil)", "fr": "French (fr)", 
             "he": "Hebrew (he)", "hi": "Hindi (hi)","hu": "Hungarian (hu)",
             "id": "Indonesian (id)","it": "Italian (it)", "ja": "Japanese (ja)",
             "ko": "Korean (ko)","msa": "Malay (msa)","nl": "Dutch (nl)", 
             "no": "Norwegian (no)", "pl": "Polish (pl)", "pt": "Portuguese (pt)",
             "ro": "Romanian (ro)","ru": "Russian (ru)", "sv": "Swedish (sv)", 
             "th": "Thai (th)", "tr": "Turkish (tr)","uk": "Ukrainian (uk)",
             "ur": "Urdu (ur)", "vi": "Vietnamese (vi)","zh": "Chinese (zh)",
             "zh-cn": "Chinese(cn)","zh-tw": "Chinese(cn)"}



def count_lang(db):
    response = temp_response
    sum = {}
    for index in db['lang']:
        language = db['lang'][index]
        num = db['Count'][index]
        if language in sum.keys():
            sum[language] += num
        else:
            sum[language] = num
    

    other_lang = {'name': '','value':0}
    for word in sum.keys():
        if word in lang_code.keys():
            for lang in lang_code.keys():
                tmp = {}
                if word == lang:
                    tmp['name'] = lang_code[lang]
                    tmp['value'] = sum[word]
                    response['data'].append(tmp)
        else:
            other_lang['name'] = 'Others'
            other_lang['value'] += sum[word]
    response['data'].append(other_lang)
    return response



@app.route('/')
def index():
    return 'hello'

@app.route('/lang_data', methods = ['GET'])
def get_timeline():
    result = {}
    for i in db:
        data = db[i]
    #result = count_lang(data)
    try:
        result = count_lang(data)
    except Exception as e:
        result['status'] = 'false'
        result['message'] = e
    else:
        result['status'] = 'true'
        result['message'] = 'None'
    return result

    




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 5000)
