// (team72, Jian, Liu, 1010361)
// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import '../theme/index.css';
import echarts from "echarts";
import axios from 'axios'
import leaflet from "leaflet";
import "leaflet/dist/leaflet.css";
import ausState from "../static/states.min.json"
import icon from 'leaflet/dist/images/marker-icon.png';
import iconShadow from 'leaflet/dist/images/marker-shadow.png';
let DefaultIcon = L.icon({
  iconUrl: icon,
  shadowUrl: iconShadow
});
L.Marker.prototype.options.icon = DefaultIcon;

Vue.use(ElementUI, {locale});
Vue.config.productionTip = false;
Vue.prototype.$echarts = echarts;
axios.defaults.publicPath = 'http://45.113.233.244'
axios.defaults.baseURL = 'http://45.113.233.244'
Vue.prototype.$axios = axios
Vue.prototype.$leaflet = leaflet
Vue.prototype.$ausState = ausState

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
