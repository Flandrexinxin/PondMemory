import { createRouter, createWebHistory, Router, RouteRecordRaw } from 'vue-router'
const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: () => import('@/views/Home.vue')
  },
  {
    path: '/setting',
    name: 'setting',
    component: () => import('@/views/Setting.vue')
  },
  {
    path: '/personal',
    name: 'personal',
    component: () => import('@/views/Personal.vue')
  },
  {
    path:'/WechatRecord',
    name:'WechatRecord',
    component:()=> import('@/views/WechatRecord.vue')
  },
]

const router: Router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
