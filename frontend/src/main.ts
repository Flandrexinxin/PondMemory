import './style.css'
import './assets/font/font.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import VueKinesis from 'vue-kinesis'
import * as echarts from 'echarts';
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.config.globalProperties.$echarts = echarts
app.use(VueKinesis)
app.use(router)
app.use(ElementPlus)
app.mount('#app')
