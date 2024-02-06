import { createRouter, createWebHistory, Router, RouteRecordRaw } from 'vue-router'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@renderer/views/Home.vue')
  }
]

const router: Router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
