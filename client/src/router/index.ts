import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ChannelView from '@/views/Home/MainView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), routes: [{
    path: '/test', name: 'test', component: HomeView,
  }, {
    path: '/', name: 'home', component: ChannelView
  }, {
    path: '/liba', name: 'liba', component: ChannelView,
  }, {
    path: '/channels', name: 'channels', component: ChannelView,
  }, {
    path: '/news', name: 'news', component: ChannelView,
  },],
})

export default router
