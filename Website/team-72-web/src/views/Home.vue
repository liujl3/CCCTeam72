<template>
  <div id="home">
    <!-- Header -->
    <header>
      <div class="header-content header-title noselect">COMP90024 - Team72</div>
      <el-menu
        :default-active="activeIndex"
        class="header-content header-nav noselect"
        mode="horizontal"
        background-color="#00000000"
        text-color="#fff"
        active-text-color="#74c0ff"
      >
        <el-menu-item index="#team">
          <a href="#team" class="nav-btn">Team</a>
        </el-menu-item>
        <el-submenu index="Works" id="work-submenu">
          <template slot="title">
            <a class="nav-btn">Works</a>
          </template>
          <el-menu-item index="#timeline" class="noselect">
            <a href="#timeline" class="nav-btn">Timeline</a>
          </el-menu-item>
          <el-menu-item index="#city" class="noselect">
            <a href="#city" class="nav-btn">City</a>
          </el-menu-item>
          <el-menu-item index="#lang" class="noselect">
            <a href="#lang" class="nav-btn">Language</a>
          </el-menu-item>
          <el-menu-item index="#map" class="noselect">
            <a href="#map" class="nav-btn">Distribution and Hospital</a>
          </el-menu-item>
        </el-submenu>
        <el-menu-item index="#introduction">
          <a href="#introduction" class="nav-btn">Introduction</a>
        </el-menu-item>
        <el-menu-item index="#title">
          <a href="#title" class="nav-btn">Home</a>
        </el-menu-item>
      </el-menu>
    </header>
    <!-- Title -->
    <div id="title" class="noselect">
      <div class="title-text">COMP90024 Project</div>
      <div class="title-text">Team 72</div>
      <br />
      <div class="title-text subtitle-text">Analysis of Australian COVID19 related Twitter</div>
    </div>
    <!-- Introduction -->
    <div id="introduction" class="content-container">
      <h2>Introduction</h2>
      <p>
        Coronavirus 2019 is an infectious disease caused by severe acute respiratory syndrome coronavirus 2.
        At present, the disease is outbreaking and spreading rapidly in various countries around the world,
        and Australia is also deeply affected.
        The current epidemic has spread to more than 200 countries and regions,
        infecting more than 5 million people and causing more than 300,000 patients to die,
        and still in Continue to spread.
      </p>
      <p>
        This project focuses on Australia's tweets related to COVID19,
        conducts statistics and analysis, and visually displays the attention of the people in different cities,
        different cities and different languages in Australia to the epidemic.
      </p>
      <p>
        Github Respository：<el-link href="https://github.com/liujl3/CCCTeam72">https://github.com/liujl3/CCCTeam72</el-link>
      </p>
    </div>
    <!-- Work -->
    <!-- time -->
    <div id="timeline" class="content-container">
      <h2>Timeline</h2>
      <el-divider></el-divider>
      <div id="timelineChart" class="chart"></div>
    </div>
    <!-- city -->

    <div id="city" class="content-container">
      <h2>State and City</h2>
      <el-divider></el-divider>
      <el-radio-group v-model="selectedState" @change="drawCityChart">
        <el-radio-button label="Total"></el-radio-button>
        <el-radio-button label="New South Wales"></el-radio-button>
        <el-radio-button label="Victoria"></el-radio-button>
        <el-radio-button label="Queensland"></el-radio-button>
        <el-radio-button label="Western Australia"></el-radio-button>
        <el-radio-button label="South Australia"></el-radio-button>
        <el-radio-button label="Tasmania"></el-radio-button>
      </el-radio-group>
      <div id="cityChart" class="chart"></div>
    </div>
    <!-- lang -->
    <div id="lang" class="content-container">
      <h2>Language</h2>
      <el-divider></el-divider>
      <div id="langChart" class="chart"></div>
    </div>
    <!-- map -->
    <div id="map" class="content-container">
      <h2>Map</h2>
      <el-divider></el-divider>
      <div id="mapChart" class="chart"></div>
    </div>
    <!-- Team -->
    <div id="team" class="content-container">
      <h2>Team</h2>
      <el-divider></el-divider>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home",
  data() {
    return {
      activeIndex: "0",
      selectedState: "Total",
      allCityData: [],
      cityChart: null
    };
  },
  methods: {
    timelineAddTotal(data) {
      var totalData = [];
      for (var i = 0; i < data[0].data.length; i++) {
        var totalDataPerDate = 0;
        for (var j = 0; j < data.length; j++) {
          totalDataPerDate += data[j].data[i];
        }
        totalData.push(totalDataPerDate);
      }
      data.unshift({
        name: "Total",
        type: "line",
        label: {
          normal: {
            show: true,
            position: "top"
          }
        },
        data: totalData
      });
      console.log(data);
      return data;
    },
    drawCityChart() {
      console.log("ccc");
      var cityData = [];
      for (var i = 0; i < this.allCityData.length; i++) {
        if (this.allCityData[i].cat == this.selectedState) {
          cityData = this.allCityData[i].data;
          break;
        }
      }
      var cityOption = {
        tooltip: {
          trigger: "item",
          formatter: "{b}: {d}%"
        },
        series: [
          {
            name: "city",
            type: "pie",
            radius: ["50%", "70%"],
            center: ["50%", "60%"],
            avoidLabelOverlap: true,
            label: {
              show: true
            },
            normal: {
              textStyle: {
                fontSize: 24
              }
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "24",
                fontWeight: "bold"
              }
            },
            labelLine: {
              show: true
            },
            data: cityData.sort(function(a, b) {
              return a.value - b.value;
            })
          }
        ]
      };
      if (this.cityChart) {
        this.cityChart.setOption(cityOption);
      } else if (this.allCityData) {
        this.cityChart = this.$echarts.init(
          document.getElementById("cityChart")
        );
        this.cityChart.setOption(cityOption);
      }
    },
    langEn(data) {
      var result = [];
      result.push(data[0]);
      result.push(data[data.length - 1]);
      var otherCount = 0;
      for (var i = 1; i < data.length - 1; i++) {
        otherCount += data[i].value;
      }
      result.push({ name: "Others", value: otherCount });
      return result;
    },
    langOther(data) {
      var result = [];
      for (var i = 1; i < data.length - 1; i++) {
        result.push(data[i]);
      }
      return result;
    }
  },
  mounted() {
    // timeline
    this.$axios
      .get("/timeline_data")
      .then(response => {
        // request success
        var result = response.data;
        if (result.status) {
          var timelineOption = {
            title: {
              // text: "Number of tweets related to covid19"
            },
            tooltip: {
              trigger: "axis"
            },
            legend: {
              data: [
                "Total",
                "New South Wales",
                "Victoria",
                "Queensland",
                "Western Australia",
                "South Australia",
                "Tasmania",
                "Australian Capital Territory",
                "Northern Territory",
                "Jervis Bay Territory"
              ]
            },
            toolbox: {
              feature: {
                saveAsImage: {}
              }
            },
            grid: {
              left: "3%",
              right: "4%",
              bottom: "3%",
              containLabel: true
            },
            xAxis: [
              {
                type: "category",
                boundaryGap: false,
                data: result.xAxis
              }
            ],
            yAxis: [
              {
                type: "value",
                max:600,
                boundaryGap: [0, "100%"]
              }
            ],
            series: this.timelineAddTotal(result.data)
          };
          console.log(timelineOption);
          var chart = this.$echarts.init(
            document.getElementById("timelineChart")
          );
          chart.setOption(timelineOption);
        }
      })
      .catch(e => {
        //Request Error
      });
    // city
    this.$axios
      .get("/city_data")
      .then(response => {
        // request success
        var result = response.data;
        if (result.status) {
          this.allCityData = result.data;
          this.cityChart = this.$echarts.init(
            document.getElementById("cityChart")
          );
          this.drawCityChart();
        }
      })
      .catch(e => {
        //Request Error
      });

    // lang
    this.$axios
      .get("/lang_data")
      .then(response => {
        // request success
        var result = response.data;
        if (result.status) {
          var langOption = {
            title: [
              {
                text: "All languages",
                left: "25%",
                textAlign: "center",
                top: 20
              },
              {
                text: "Other languages",
                left: "75%",
                textAlign: "center",
                top: 20
              }
            ],

            tooltip: {
              trigger: "item",
              formatter: "{b} : {d}%"
            },
            series: [
              {
                name: "All:",
                type: "pie",
                radius: "60%",
                center: ["25%", "50%"],
                data: this.langEn(result.data).sort(function(a, b) {
                  return a.value - b.value;
                }),

                animationType: "scale",
                animationEasing: "elasticOut",
                animationDelay: function(idx) {
                  return Math.random() * 200;
                }
              },
              {
                name: "Others:",
                type: "pie",
                radius: "60%",
                center: ["75%", "50%"],
                data: this.langOther(result.data).sort(function(a, b) {
                  return a.value - b.value;
                }),

                animationType: "scale",
                animationEasing: "elasticOut",
                animationDelay: function(idx) {
                  return Math.random() * 200;
                }
              }
            ]
          };
          var chart = this.$echarts.init(document.getElementById("langChart"));
          chart.setOption(langOption);
        }
      })
      .catch(e => {
        //Request Error
      });
    // map
  }
};
</script>
<style>
header {
  z-index: 100;
  /* display: -webkit-flex;
  display: inline-flex; */
  /* flex-direction: row; */
  width: 100%;
  /* align-items:center; */
  border-bottom: 1px solid rgb(163, 163, 163);
  position: fixed;
  top: 0;
  left: 0;
  background-color: #000000aa;
  border-radius: 0 0 0.3em 0.3em;
}
.header-content {
  /* height: 4em; */
  line-height: 3.8em;
  margin: 0 2em;
}
.header-title {
  font-weight: bold;
  color: #a0d4ff;
  text-align: left;
  float: left;
}
.header-nav {
  border: 0px !important;
  float: right;
}
.header-nav > .el-menu-item,
.header-nav > .el-submenu {
  float: right !important;
}
.nav-btn {
  color: white;
  text-decoration: none;
}
#title {
  border-radius: 0.3em;
  /* margin-top:3.8em; */
  background-image: url("../assets/background.jpg");
  background-attachment: fixed;
  background-size: cover;
  width: 100%;
  padding: 8em 0;
}
.title-text {
  font-weight: bold;
  font-size: 48px;
  color: white;
  padding-top: 0.5em;
  text-shadow: 3px 3px 3px black;
}
.subtitle-text {
  font-weight: normal;
  font-size: 20px;
  padding-top: 1em;
  /* padding-bottom: 1em; */
}
#introduction {
  text-align: left;
}
.el-menu--popup {
  background-color: #000000aa !important;
}
.content-container {
  margin: 2em;
  border-radius: 0.3em;
  box-shadow: 0px 0px 5px 0px rgb(202, 202, 202);
  background-color: rgb(245, 245, 245);
  /* color:white */
  padding: 3em 6em;
  text-align: left;
}
.chart {
  width: 100%;
  height: 640px;
}
h3 {
  text-decoration: underline;
}
</style>