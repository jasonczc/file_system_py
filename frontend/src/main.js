import Vue from 'vue'
import App from './App.vue'
import Vuetify from "vuetify";
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import '@mdi/font/css/materialdesignicons.css'
import zhHans from 'vuetify/es5/locale/zh-Hans'
//import router from "@/router/router";
Vue.config.productionTip = false
Vue.use(Vuetify, {
  directives: {
    Touch
  }
});
const vuetify = new Vuetify({
  theme: {
    dark: false,
    themes: {
      dark: {
        primary: 'green',
        info: 'green'
      }
    },
    lang: {
      locales: { zhHans},
      current: 'zhHans',
    },
  },
});

new Vue({
  vuetify,
  //router,
  render: h => h(App)
}).$mount('#app')
