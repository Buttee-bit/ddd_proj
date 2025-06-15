import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainView from '@/views/Layout.vue'
import ChannelView from '@/views/Home/ChannelsView.vue'
import BaseKnow from '@/views/Home/BaseKnow.vue'
import News from '@/views/Home/News.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), routes: [{
    path: '/test', name: 'test', component: HomeView,
  }, {
    path: '/', name: 'home', component: HomeView
  }, {
    path: '/liba', name: 'liba', component: BaseKnow,
  }, {
    path: '/channels', name: 'channels', component: ChannelView,
  }, {
    path: '/news', name: 'news', component: News,
  },],
})

export default router
