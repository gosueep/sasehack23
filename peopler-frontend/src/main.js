import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/global.css'

import { fas } from '@fortawesome/free-solid-svg-icons'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
library.add(fas)

createApp(App).component('fa-icon', FontAwesomeIcon).use(router).mount('#app')
