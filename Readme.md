## COMP90024 Assignment 2 - City Analytics on	the	Cloud

This project focuses on Australia's tweets related to COVID19, conducts statistics and analysis, and visually displays the attention of the people in different cities, different cities and different languages in Australia to the epidemic.

## Automation guide

1. Virtual machine operating system: NeCTAR CentOS 7 x86_64.

2. Open port(TCP):
- Database server: 5984, 4369, 9100-9200
- Web server: 80

3. `cd` to user floder and clone this repository.

4. Write the addresses of the CouchDB server in `Automation/hosts` file.

5. Save your private key file as `private.pem` and put it in the `Automation` folder, this private key will be used to connect to all database servers, all database server has same account: `admin:123456`.

> *run `Automation/process.sh` to collect and process data (Need to provide Twitter search API access authentication).*

6. Then run `Automation/deploy.sh` as a system administrator.

## Main Technology Stacks
- **Database**: CouchDB cluster
- **Harvest**: Twitter development api
- **Data Analysis**: MapReduce Views
- **WebServer**: Flask RESTful api server, Nginx Reverse proxy
- **Website**: Vue.js singe page application, Element-UI for UI
- **Data Visualization**: Echarts for charts, leaftlet with GeoJSON for map