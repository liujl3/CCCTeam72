#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {
    ## timeline_data
        "status": True,
        "message": "error message",
        
        "xAxis": ["05/10", "05/11", "05/12", "05/13", "05/14", "05/15", "05/16"],
        "data": [
            {
                "name": "Total", "type": "line", "stack": "volume", 
                "data": [100,100,100,100,100,100,100]
            },
            {
                "name": "Total", "type": "line", "stack": "volume", 
                "data": [100,100,100,100,100,100,100]
            }
        ]
    },
    {
    # city_data
        "status": True,
        "message": "error message",
        
        "data":[
            {
                "cat": "Total", 
                "data":[
                    {"name":"Melbourne","value":1200},
                    {"name":"Melbourne","value":1200},
                    {"name":"Melbourne","value":1200}
                ]
            },
            {
                "cat": "NSW", 
                "data":[
                    {"name":"Melbourne","value":1200},
                    {"name":"Melbourne","value":1200},
                    {"name":"Melbourne","value":1200}
                ]
            }
        ]
    },
    # lang_data
    {
        "status": True,
        "message": "error message",
        
        "data":[
            {"name":"English","value":1200},
            {"name":"Chinese","value":1200}
        ]
    },
    # dot_data
    {
        "status": True,
        "message": "error message",
        
        "tweets":[
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"}
        ],
        "hospitals":[
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
            {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"}
        ]
    }
]

@app.route('/api/data/<string:name>', methods=['GET'])
def get_data(name):
    if name == 'timeline':
        return jsonify({'timeline_data': data[0]})
    elif name == 'city':
        return jsonify({'city_data': data[1]})
    elif name == 'lang':
        return jsonify({'city_data': data[2]})
    elif name == 'dot':
        return jsonify({'city_data': data[3]})
    else:
        return jsonify({'Error! Data not found!'})



if __name__ == '__main__':
    app.run(debug=True)






