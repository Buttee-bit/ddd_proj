import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '@/views/Home/HomeView.vue'
import ChannelView from '@/views/Channels/ChannelsView.vue'
import BaseKnow from '@/views/BaseKnow/BaseKnow.vue'
import News from '@/views/News/News.vue'
import AddChannel from "@/views/Channels/AddChannel.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [{
        path: '/test/', name: 'test', component: HomeView,
    }, {
        path: '/', name: 'home', component: HomeView
    }, {
        path: '/liba', name: 'liba', component: BaseKnow,
    }, {
        path: '/channels',
        name: 'channels',
        component: ChannelView,

    },
        {
            path: '/channels/add',
            name: 'addChannel',
            component: AddChannel
        },
        {
        path: '/news', name: 'news', component: News,
    },],
})

export default router
