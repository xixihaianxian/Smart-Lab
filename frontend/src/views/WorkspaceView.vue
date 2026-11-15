<script setup>
import { computed } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ArrowRight, Calendar, ChatLineRound, Grid } from '@element-plus/icons-vue'

const route = useRoute()
const router = useRouter()
const pages = {
  labs: {
    label: 'EXPLORE SPACES',
    title: '探索实验室',
    description: '在这里查找适合研究的实验空间。',
    emptyTitle: '实验室信息即将呈现',
    emptyDescription: '空间目录尚未接入，待实验室信息发布后即可在这里浏览和预约。',
    icon: Grid,
  },
  reservations: {
    label: 'YOUR RESERVATIONS',
    title: '我的预约',
    description: '每一次实验安排，都清晰可见。',
    emptyTitle: '这里还没有预约记录',
    emptyDescription: '完成预约后，相关安排会出现在这里。',
    icon: Calendar,
  },
  help: {
    label: 'SUPPORT',
    title: '使用帮助',
    description: '了解如何使用 SmartLab 安排实验空间。',
    emptyTitle: '预约流程',
    emptyDescription: '进入实验室预约，选择空间和时间；确认信息后，即可在“我的预约”查看安排。',
    icon: ChatLineRound,
  },
}
const page = computed(() => pages[route.name] || pages.labs)
</script>

<template>
  <section class="workspace-page">
    <p class="eyebrow"><span></span> {{ page.label }}</p>
    <h1>{{ page.title }}</h1>
    <p class="workspace-description">{{ page.description }}</p>
    <div class="empty-panel">
      <div class="empty-icon"><el-icon :size="30"><component :is="page.icon" /></el-icon></div>
      <h2>{{ page.emptyTitle }}</h2>
      <p>{{ page.emptyDescription }}</p>
      <el-button v-if="route.name === 'reservations'" class="empty-action" @click="router.push('/labs')">
        浏览实验室 <el-icon><ArrowRight /></el-icon>
      </el-button>
      <el-button v-if="route.name === 'help'" class="empty-action" @click="router.push('/')">
        返回工作台 <el-icon><ArrowRight /></el-icon>
      </el-button>
    </div>
  </section>
</template>
