<template>
  <div id="app">
    <!-- (team72, Jian, Liu, 1010361) -->
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
  beforeCreate(){
    if(this.$route.path!="/"){
      this.$router.push("/")
    }
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body {
  margin: 0;
  padding: 0;
  /* background-color: rgb(54, 54, 54); */
}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Chrome/Safari/Opera */
  -khtml-user-select: none; /* Konqueror */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently*/
}
</style>
