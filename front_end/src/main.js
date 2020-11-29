// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import VCharts from 'v-charts'
import ElementUI from 'element-ui'
import '../node_modules/echarts/map/js/world.js' // 引入世界地图
import messageNotice from "./components/messageNotice";
import echarts from 'echarts'
Vue.use(echarts)
Vue.use(VCharts)
Vue.use(ElementUI)
Vue.component(messageNotice.name,messageNotice)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
