import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
    {path: '/word', component: 'WordCloud'},
    {path: '/map', component: 'Map'},
    {path: '/lineChart',component: 'LineChart'},
    {path: '/barChart',component: 'BarChart'},
    {path: '/roseMap',component: 'RoseMap'},
    {path: '/', component: 'Home'},
    {path: '/about', component: 'About'},
    {path: '*', component: 'NotFound'}

]
const routes = routerOptions.map(route => {
    return {
        ...route,
        component: () => import(`@/components/${route.component}.vue`)
    }
})
Vue.use(Router)
export default new Router({
    routes,
    mode: 'history'
})
