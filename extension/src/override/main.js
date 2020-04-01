import Vue from 'vue'
import App from './App.vue'
import store from '@/store/store.js'
import ress from 'ress'


/* eslint-disable no-new */
new Vue({
  el: '#app',
  store,
  render: h => h(App)
})
