import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './vue'
import router from './router'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'



const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  component(key, component)
}
use(ElementPlus)
use(createPinia())
use(router)

mount('#app')
