import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView, meta: { title: '工作台' } },
    {
      path: '/labs',
      name: 'labs',
      component: () => import('../views/WorkspaceView.vue'),
      meta: { title: '实验室预约' },
    },
    {
      path: '/reservations',
      name: 'reservations',
      component: () => import('../views/WorkspaceView.vue'),
      meta: { title: '我的预约' },
    },
    {
      path: '/help',
      name: 'help',
      component: () => import('../views/WorkspaceView.vue'),
      meta: { title: '使用帮助' },
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue'),
      meta: { title: '登录' },
    },
    {
      path: '/register',
      name: 'register',
      component: () => import('../views/register.vue'),
      meta: { title: '注册' },
    },
    { path: '/:pathMatch(.*)*', redirect: '/' },
  ],
})

export default router
