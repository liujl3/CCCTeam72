## COMP90024 Assignment 2 - City Analytics on	the	Cloud

This project focuses on Australia's tweets related to COVID19, conducts statistics and analysis, and visually displays the attention of the people in different cities, different cities and different languages in Australia to the epidemic.

## Automation guide

1. Virtual machine operating system image: NeCTAR CentOS 7 x86_64.

2. Security Group Open Port(TCP):
- Database server: 5984, 4369, 9100-9200
- Web server: 80

3. `SSH` connect to web server, `cd` to user floder and clone this repository.

4. Write the addresses of the CouchDB server in `Automation/hosts` file.

5. Change the databse server address in `Website/flask_app.py`.

6. Save your private key file as `private.pem` and put it in the `Automation` folder, this private key will be used to connect to all database servers, all database server has same account: `admin:123456`.

    > *run `Automation/process.sh` to collect and process data (Need to provide valid Twitter search API access authentication).*

7. Then run `Automation/deploy.sh` as a system administrator.

## System architecture
In this project, we use 4 virtual machine on UniMelb Research Cloud, one for web server and data processing, and the other three instances formed a database cluster. After collecting data from tweeter API and processing data by using MapReduce, the API server organizes the data into a web page understandable format and returns it when the web page calls these APIs, and then the web page draws the chart through the corresponding library.

## Main Technology Stacks
- **Database**: CouchDB cluster
- **Harvest**: Twitter development API
- **Data Analysis**: MapReduce Views
- **WebServer**: Flask RESTful api server, Nginx reverse proxy
- **Website**: Vue.js singe page application, Element-UI for UI
- **Data Visualization**: Echarts for charts, leaftlet with GeoJSON for map