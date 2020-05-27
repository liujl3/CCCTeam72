## COMP90024 Assignment 2 - City Analytics on the	Cloud

This project focuses on Australia's tweets related to COVID19, conducts statistics and analysis, and visually displays the attention of the people in different cities, different cities and different languages in Australia to the epidemic. 

The video demo of this project is available on [https://www.youtube.com/watch?v=8MdzP73Syk0.](https://www.youtube.com/watch?v=8MdzP73Syk0)

## Automation Guide

1. Virtual machine operating system image: NeCTAR CentOS 7 x86_64.

2. Security Group Open Port(TCP):
    - Database server: 5984, 4369, 9100-9200
    - Web server: 80

3. `SSH` connect to web server, `cd` to user folder and clone this repository.

- run [Automation](https://github.com/liujl3/CCCTeam72/tree/master/Automation)/[deploy_website_only.sh](https://github.com/liujl3/CCCTeam72/blob/master/Automation/deploy_website_only.sh) without following steps can only deploy website on current instance, this can directly access the data in the existing database.

4. Write the addresses of the CouchDB server in  [Automation](https://github.com/liujl3/CCCTeam72/tree/master/Automation)/[hosts](https://github.com/liujl3/CCCTeam72/blob/master/Automation/hosts) file.

5. Change the database server address in [Website](https://github.com/liujl3/CCCTeam72/tree/master/Website)/[flask_app.py](https://github.com/liujl3/CCCTeam72/blob/master/Website/flask_app.py).

6. Save your private key file as `private.pem` and put it in the  [Automation](https://github.com/liujl3/CCCTeam72/tree/master/Automation) folder, this private key will be used to connect to all database servers, all database server has same account: `admin:123456`.

    > *run [Automation](https://github.com/liujl3/CCCTeam72/tree/master/Automation)/[process.sh](https://github.com/liujl3/CCCTeam72/blob/master/Automation/process.sh) to collect and process data (Need to provide valid Twitter search API access authentication).*

7. Then run  [Automation](https://github.com/liujl3/CCCTeam72/tree/master/Automation)/[deploy.sh](https://github.com/liujl3/CCCTeam72/blob/master/Automation/deploy.sh) as a system administrator.

## System Architecture
In this project, we use 4 virtual machine on [Unimelb Research Cloud](https://dashboard.cloud.unimelb.edu.au), one for web server and data processing, and the other three instances formed a database cluster. After collecting data from tweeter API and processing data by using MapReduce, the API server organizes the data into a web page understandable format and returns it when the web page calls these APIs, and then the web page draws the chart through the corresponding library.

## Main Technology Stacks
- **Database**: [CouchDB](https://couchdb.apache.org/) cluster
- **Harvest**: [Twitter development API](https://developer.twitter.com/en/docs/tweets/search/api-reference)
- **Data Analysis**: MapReduce Views
- **Webserver**: [Flask](https://flask.palletsprojects.com/en/1.1.x/) RESTful API server, [Nginx](http://nginx.org/en/) reverse proxy
- **Website**: [Vue.js](https://vuejs.org/index.html) for single page application, [Element-UI](https://element.eleme.cn/#/en-US) for UI, [Webpack](https://webpack.js.org/) for pack all resources
- **Data Visualization**: [Echarts](https://echarts.apache.org/en/index.html) for charts, [leaftlet](https://leafletjs.com/) with [GeoJSON](https://geojson.org/) for map

## Team Contribution

- **Decheng Wang**:Data Collection,  Environment Setting, Web Server Design and Implementation, Report Writing.
- **Siyuan Wu**: Data Collection, Data Analysis, CouchDB View, Report Writing.
- **Dongfang Wang**: Data Collection, Data  Analysis, YouTube Video, Presentation, Report Writing.
- **Jian Liu**: Environment Setting, Data Collection, Web Page Design and Implementation, Data Visualization, Automation.