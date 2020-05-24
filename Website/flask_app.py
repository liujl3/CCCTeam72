from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import couchdb
app = Flask(__name__)




database_name = "city_lang_results"
database_host = "http://admin:123456@45.113.235.44:80/"
database_server = couchdb.Server(database_host)
db = database_server["city_lang_results"]


temp_response =[{
    "status": True,
    "message": "error message",
    
    "data":[]
    }]




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
    try:
        reponse = count_lang(db)
    except e:
        response['status'] = False
        response['message'] = e
    else:
        response['status'] = True
        response['message'] = 'None'


        
        return response



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port = 5000)
