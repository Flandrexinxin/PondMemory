import { createRouter, createWebHistory } from 'vue-router'
const routes = [
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

const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router
