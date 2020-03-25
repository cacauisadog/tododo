import Vue from 'vue'
import Vuex from 'vuex'
import api from '~api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    currentUser: undefined
  },
  mutations: {
    setCurrentUser (state, currentUser) {
      console.log('set logged user: ' + JSON.stringify(currentUser))
      state.currentUser = currentUser
    },
    removeCurrentUser (state) {
      state.currentUser = null
    }
  },
  getters: {
    currentUser (state) {
      return state.currentUser
    }
  },
  actions: {
    whoami ({ commit }) {
      return api.auth.whoami().then(user => {
        if (user.is_authenticated) {
          commit('setCurrentUser', user)
        } else {
          commit('removeCurrentUser')
        }
      })
    }
  },
  modules: {}
})
