<script setup>
import { computed, ref, watch } from 'vue'
import logoUrl from '@/assets/icons/logo.svg'
import { useRoute, useRouter } from 'vue-router'
import {
  ArrowRight,
  Calendar,
  ChatLineRound,
  Grid,
  House,
  Menu as MenuIcon,
  Moon,
  Sunny,
} from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()
const mobileMenuOpen = ref(false)
const today = computed(() =>
  new Intl.DateTimeFormat('zh-CN', {
    month: 'long',
    day: 'numeric',
    weekday: 'long',
  }).format(new Date()),
)

const navigation = [
  { path: '/', label: '工作台', icon: House },
  { path: '/labs', label: '实验室预约', icon: Grid },
  { path: '/reservations', label: '我的预约', icon: Calendar },
]

watch(
  () => route.path,
  () => {
    mobileMenuOpen.value = false
  },
)

function navigate(path) {
  mobileMenuOpen.value = false
  router.push(path)
}
</script>

<template>
  <div v-if="route.name === 'login' || route.name === 'register'" class="login-route">
    <router-view />
  </div>
  <div v-else class="app-shell">
    <header class="topbar">
      <div class="topbar-brand">
        <el-button
          class="mobile-menu-button"
          text
          circle
          aria-label="打开导航菜单"
          @click="mobileMenuOpen = true"
        >
          <el-icon :size="21"><MenuIcon /></el-icon>
        </el-button>
        <router-link to="/" class="brand-link" aria-label="Smart Lab 首页">
          <img class="brand-mark" :src="logoUrl" alt="" width="42" height="42" />
          <span class="brand-name">Smart<span>Lab</span><small>实验室预约平台</small></span>
        </router-link>
      </div>

      <div class="topbar-right">
        <span class="today"><el-icon><Sunny /></el-icon>{{ today }}</span>
        <span class="topbar-divider"></span>
        <router-link to="/login" class="account-link" aria-label="前往登录页面">
          <span class="user-avatar" aria-hidden="true">S</span>
          <span class="user-name">你好，访客</span>
        </router-link>
      </div>
    </header>

    <div class="shell-body">
      <aside class="sidebar" aria-label="侧边导航">
        <div class="sidebar-inner">
          <p class="menu-caption">工作空间</p>
          <nav class="side-nav" aria-label="主导航">
            <button
              v-for="item in navigation"
              :key="item.path"
              type="button"
              class="nav-item"
              :class="{ 'is-active': route.path === item.path }"
              :aria-current="route.path === item.path ? 'page' : undefined"
              @click="navigate(item.path)"
            >
              <el-icon :size="19"><component :is="item.icon" /></el-icon>
              <span>{{ item.label }}</span>
              <el-icon v-if="route.path === item.path" class="nav-arrow" :size="15"><ArrowRight /></el-icon>
            </button>
          </nav>

          <div class="sidebar-separator"></div>
          <p class="menu-caption">支持</p>
          <nav class="side-nav" aria-label="帮助导航">
            <button
              type="button"
              class="nav-item"
              :class="{ 'is-active': route.path === '/help' }"
              :aria-current="route.path === '/help' ? 'page' : undefined"
              @click="navigate('/help')"
            >
              <el-icon :size="19"><ChatLineRound /></el-icon>
              <span>使用帮助</span>
              <el-icon v-if="route.path === '/help'" class="nav-arrow" :size="15"><ArrowRight /></el-icon>
            </button>
          </nav>

          <div class="sidebar-note">
            <span class="note-symbol"><el-icon :size="20"><Moon /></el-icon></span>
            <strong>让研究更专注</strong>
            <p>把时间留给探索，空间交给我们安排。</p>
          </div>
          <div class="sidebar-footer">© {{ new Date().getFullYear() }} SmartLab</div>
        </div>
      </aside>

      <main class="main-content" id="main-content">
        <div class="content-wrap">
          <div class="content-topline">
            <span class="breadcrumb">工作空间 <span>/</span> {{ route.meta.title || '工作台' }}</span>
            <span class="topline-label"><span class="status-dot"></span> 空间预约服务</span>
          </div>
          <router-view />
        </div>
      </main>
    </div>

    <el-drawer v-model="mobileMenuOpen" direction="ltr" size="min(290px, 85vw)" :with-header="false" class="mobile-drawer">
      <div class="drawer-brand">Smart<span>Lab</span></div>
      <p class="menu-caption">工作空间</p>
      <nav class="side-nav" aria-label="移动端主导航">
        <button
          v-for="item in navigation"
          :key="item.path"
          type="button"
          class="nav-item"
          :class="{ 'is-active': route.path === item.path }"
          @click="navigate(item.path)"
        >
          <el-icon :size="19"><component :is="item.icon" /></el-icon>{{ item.label }}
        </button>
        <button type="button" class="nav-item" :class="{ 'is-active': route.path === '/help' }" @click="navigate('/help')">
          <el-icon :size="19"><ChatLineRound /></el-icon>使用帮助
        </button>
      </nav>
    </el-drawer>
  </div>
</template>
