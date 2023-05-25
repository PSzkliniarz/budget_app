import Vue from 'vue'
import Vuex from 'vuex'
import axiosInstance from "@/axios-api";

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    APIData: '',
    category: ''
  },
  getters: {
    loggedIn (state) {
      return state.accessToken != null
    }
  },
  mutations: {
    updateStorage(state, {access, refresh}) {
      state.accessToken = access
      state.refreshToken = refresh
    },
    destroyToken (state) {
      state.accessToken = null
      state.refreshToken = null
    }
  },
  actions: {
    userLogout (context) {
      if (context.getters.loggedIn) {
          context.commit('destroyToken')
      }
    },
    userLogin(context, userCredentials) {
      return new Promise((resolve) => {
        axiosInstance.post('/api-token/', {
          username: userCredentials.username,
          password: userCredentials.password
        })
            .then(response => {
              context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh});
              resolve();
            });
      });
}

  },
  modules: {
  }
})
