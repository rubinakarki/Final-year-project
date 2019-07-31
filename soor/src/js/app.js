import Vue from 'vue';
import App from './App.vue';
import VueChatScroll from 'vue-chat-scroll';
import BootstrapVue from 'bootstrap-vue';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import VueYoutube from 'vue-youtube';



Vue.config.productionTip = false;
Vue.use(VueChatScroll);
Vue.use(BootstrapVue);
Vue.use(VueYoutube);

new Vue({
  render: h => h(App)
}).$mount('#app')
