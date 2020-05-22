<template>
  <div id="home">
    <!-- Header -->
    <header>
      <div class="header-content header-title noselect">COMP90024 - Team72</div>
      <el-menu
        :default-active="activeIndex"
        class="header-content header-nav noselect"
        mode="horizontal"
        @select="handleSelect"
        background-color="#00000000"
        text-color="#fff"
        active-text-color="#74c0ff"
      >
        <el-menu-item index="3"> <a href="#team" class="nav-btn">Team</a></el-menu-item>
        <el-submenu index="2" id="work-submenu">
          <template slot="title"><a class="nav-btn">Works</a></template>
          <el-menu-item index="2-1" class="noselect"> <a href="#timeline" class="nav-btn">Timeline</a></el-menu-item>
          <el-menu-item index="2-2" class="noselect"> <a href="#geography" class="nav-btn">Geography</a></el-menu-item>
          <el-menu-item index="2-3" class="noselect"> <a href="#language" class="nav-btn">Language</a></el-menu-item>
          <el-menu-item index="2-4" class="noselect"> <a href="#age" class="nav-btn">Age</a></el-menu-item>
        </el-submenu>
        <el-menu-item index="1"> <a href="#introduction" class="nav-btn">Introduction</a></el-menu-item>
        <el-menu-item index="0">  <a href="#title" class="nav-btn">Home</a></el-menu-item>
      </el-menu>
    </header>
    <!-- Title -->
    <div id="title" class="noselect">
      <div class="title-text">COMP90024 Project</div>
      <div class="title-text">Team 72</div>
      <div class="title-text subtitle-text">Analysis of Australian COVID19 related Twitter</div>
    </div>
    <!-- Introduction -->
    <div id="introduction">
      <div>
      introduction
      </div>
      <div>
      introduction
      </div>
      <div>
      introduction
      </div>
      <div>
      introduction
      </div>
      introduction
      introduction
      introduction
      introduction
      introduction
      introduction
      introduction
      introduction
      introduction
      </div>
    <!-- Work -->
    <!-- time -->
    <!-- geo -->
    <!-- lang -->
    <!-- age -->
    <!-- Team -->
  <div id="team">
    <el-divider></el-divider>
  </div>
  </div>
</template>
<script>
export default {
  name: "Home",
  data() {
    return {
      activeIndex: "0"
    };
  },
  methods: {
    handleSelect() {}
  }
};
</script>
<style>
header {
  /* display: -webkit-flex;
  display: inline-flex; */
  /* flex-direction: row; */
  width: 100%;
  /* align-items:center; */
  border-bottom: 1px solid rgb(163, 163, 163);
  position:fixed;
  top:0;
  left: 0;
  background-color: #000000AA;
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
.nav-btn{
  color: white;
  text-decoration:none;
}
#title {
  /* margin-top:3.8em; */
  background-image: url("../assets/background.jpg");
  background-attachment: fixed;
  background-size: cover;
  width: 100%;
  padding: 8em 0;
}
.title-text{
  font-weight: bold;
  font-size: 48px;
  color: white;
  padding-top: 0.5em;
  text-shadow: 3px 3px 3px black;
}
.subtitle-text{
  font-weight: normal;
  font-size: 20px;
  padding-top: 1em;
  padding-bottom: 1em;
}
#introduction{
  box-shadow: 0px 0px 5px 0px rgb(202, 202, 202) inset;
  /* color:white */
  padding: 2em 0;
}
.el-menu--popup{
  background-color: #000000AA !important;
}
</style>