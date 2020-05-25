### APIs

#### /timeline_data

method : GET

parameters: None

```json
{
    "status": true,
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
}
```

#### /city_data

method: GET

parameters: None

Response:

```json
{
    "status": true,
    "message": "error message",
    
    "data":[
        {
            "cat": "Total", 
            "tweets":[
                {"name":"Melbourne","value":1200},
                {"name":"Melbourne","value":1200},
                {"name":"Melbourne","value":1200}
            ],
            "hospitals":[
                {"name":"Melbourne","value":1},
                {"name":"Melbourne","value":2},
                {"name":"Melbourne","value":3}
            ]
        },
        {
            "cat": "NSW", 
            "tweets":[
                {"name":"Melbourne","value":1200},
                {"name":"Melbourne","value":1200},
                {"name":"Melbourne","value":1200}
            ],
            "hospitals":[
                {"name":"Melbourne","value":1},
                {"name":"Melbourne","value":2},
                {"name":"Melbourne","value":3}
            ]
        }
    ]
}
```

#### /lang_data

method: GET

parameters: None

Response:

```json
{
    "status": true,
    "message": "error message",
    
    "data":[
        {"name":"English","value":1200},
        {"name":"Chinese","value":1200}
    ]
}
```

#### /dot_data

method: GET

parameters: None

Response:

```json
{
    "status": true,
    "message": "error message",
    
    "tweets":[
        {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
        {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"},
        {"coordinate":[121.15,43], "state": "VIC", "city": "Melbourne"}
    ]
}
```

