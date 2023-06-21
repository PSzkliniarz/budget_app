import Vue from 'vue'
import Vuex from 'vuex'
import axiosInstance from "@/axios-api";

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        accessToken: null,
        refreshToken: null,

        expenses: '',
        categories: '',
        actualExpenses: ''
    },
    getters: {
        loggedIn(state) {
            return state.accessToken != null
        },
        getExpenses: (state) => state.expenses,
        getCategories: (state) => state.categories,
        getActualExpenses: (state) => state.actualExpenses
    },
    mutations: {
        updateStorage(state, {access, refresh}) {
            state.accessToken = access
            state.refreshToken = refresh

            state.expenses = ''
            state.categories = ''
            state.actualExpenses = ''
        },
        destroyToken(state) {
            state.accessToken = null
            state.refreshToken = null
        },

        SET_EXPENSES(state, payload) {
            state.expenses = payload
        },
        SET_CATEGORIES(state, payload) {
            state.categories = payload
        },
        SET_ACTUAL_EXPENSES(state, payload) {
            state.actualExpenses = payload
        }
    },
    actions: {
        userLogout(context) {
            if (context.getters.loggedIn) {
                context.commit('destroyToken')
            }
        },
        userLogin(context, userCredentials) {
            return new Promise((resolve, reject) => {
                axiosInstance.post('/api-token/', {
                    username: userCredentials.username,
                    password: userCredentials.password
                })
                    .then(response => {
                        context.commit('updateStorage', {access: response.data.access, refresh: response.data.refresh});
                        resolve();
                    })
                    .catch(error => {
                        reject(error);
                    });
            });
        },
        loadExpenses({commit}) {
            axiosInstance.get('/expense/')
                .then(response => {
                    commit('SET_EXPENSES', response.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        loadCategories({commit}) {
            axiosInstance.get('/category/')
                .then(response => {
                    commit('SET_CATEGORIES', response.data)
                })
                .catch(err => {
                    console.log(err)
                })
        },
        setActualExpenses({commit}, actualExpenses) {
            commit('SET_ACTUAL_EXPENSES', actualExpenses)
        }

    },
    modules: {}
})
