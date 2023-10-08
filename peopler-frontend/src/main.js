import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/global.css'

import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas)
library.add(far)

const app = createApp(App).component('fa-icon', FontAwesomeIcon).use(router)
app.config.globalProperties.$api_base_url = 'http://localhost:8000'
app.mount('#app')
