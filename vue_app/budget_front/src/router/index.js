import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requiresLogin: true
    }
  },
  {
    path: '/categories',
    name: 'categories',
    component: () => import(/* webpackChunkName: "login" */ '../views/CategoryView.vue'),
     meta: {
      requiresLogin: true
    }
  },
  {
    path: '/login',
    name: 'login',
    component: () => import(/* webpackChunkName: "login" */ '../views/Login.vue')
  },
  {
    path: '/registration',
    name: 'registration',
    component: () => import(/* webpackChunkName: "login" */ '../views/RegistrationView')
  },
  {
    path: '/logout',
    name: 'logout',
    component: () => import(/* webpackChunkName: "login" */ '../views/Logout.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
