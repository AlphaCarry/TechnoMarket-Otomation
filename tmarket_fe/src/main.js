import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import {createPinia} from "pinia";
import {router} from "@/rotalar/routes.js";

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import {
    faCartShopping,
    faCircleExclamation,
    faMapLocationDot,
    faPhone,
    faUserTie
} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add([faCartShopping,faMapLocationDot,faPhone,faUserTie,faCircleExclamation])
const pinia= createPinia();
const app=createApp(App)

app.use(pinia);
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app');


//createApp(App).use(createPinia()).mount('#app')