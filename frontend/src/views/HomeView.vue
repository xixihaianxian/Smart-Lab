<script setup>
import { useRouter } from 'vue-router'
import { ArrowRight, Calendar, Check, Grid, Right, Search } from '@element-plus/icons-vue'

const router = useRouter()
const steps = [
  { number: '01', title: '浏览实验室', description: '找到适合当前研究任务的空间与设备。', icon: Search },
  { number: '02', title: '选择时间', description: '按自己的日程安排合适的使用时段。', icon: Calendar },
  { number: '03', title: '开始探索', description: '确认预约信息，准备开启实验。', icon: Check },
]
</script>

<template>
  <div class="home-page">
    <section class="welcome-heading">
      <div>
        <p class="eyebrow"><span></span> WELCOME TO SMARTLAB</p>
        <h1>你好，准备好开始今天的探索了吗？</h1>
        <p class="heading-description">从一间合适的实验室开始，让每一次灵感都有空间发生。</p>
      </div>
      <span class="heading-date">SMART SPACE · BETTER RESEARCH</span>
    </section>

    <section class="hero" aria-labelledby="hero-title">
      <div class="hero-copy">
        <span class="hero-kicker"><span class="kicker-line"></span> SPACE FOR DISCOVERY</span>
        <h2 id="hero-title">理想空间，<br />让探索<span>自在发生。</span></h2>
        <p>寻找实验空间，规划使用时间。<br />让预约更轻松，让研究更从容。</p>
        <el-button class="hero-button" size="large" @click="router.push('/labs')">
          探索实验室 <el-icon class="button-arrow"><ArrowRight /></el-icon>
        </el-button>
        <span class="hero-index">01 / 01 <span>—</span> SMART LAB</span>
      </div>
      <div class="hero-visual" aria-hidden="true">
        <div class="orbit orbit-outer"></div>
        <div class="orbit orbit-middle"></div>
        <div class="orbit orbit-inner"></div>
        <div class="visual-core"><el-icon :size="48"><Grid /></el-icon></div>
        <span class="visual-star star-one">✦</span>
        <span class="visual-star star-two">✳</span>
        <span class="visual-coordinate">S / L — SMART SPACE</span>
      </div>
    </section>

    <section class="overview" aria-label="预约概览">
      <div class="overview-intro">
        <div class="section-label">YOUR WORKSPACE <span>·</span> 01</div>
        <h2>从这里，开启你的研究日常。</h2>
        <p>选择你需要的空间，轻松安排下一次实验。</p>
      </div>
      <div class="overview-actions">
        <button class="action-link" type="button" @click="router.push('/labs')">
          <span class="action-icon"><el-icon :size="21"><Grid /></el-icon></span>
          <span class="action-text"><strong>寻找实验室</strong><small>浏览适合你的实验空间</small></span>
          <el-icon class="action-arrow"><Right /></el-icon>
        </button>
        <button class="action-link" type="button" @click="router.push('/reservations')">
          <span class="action-icon"><el-icon :size="21"><Calendar /></el-icon></span>
          <span class="action-text"><strong>我的预约</strong><small>查看和管理预约安排</small></span>
          <el-icon class="action-arrow"><Right /></el-icon>
        </button>
      </div>
    </section>

    <section class="steps-section" aria-labelledby="steps-title">
      <div class="steps-heading">
        <div>
          <div class="section-label">HOW IT WORKS <span>·</span> 02</div>
          <h2 id="steps-title">预约，从未如此简单。</h2>
        </div>
        <span>三个步骤，开启你的实验之旅</span>
      </div>
      <div class="steps-grid">
        <div v-for="step in steps" :key="step.number" class="step-item">
          <span class="step-number">{{ step.number }}</span>
          <div class="step-icon"><el-icon :size="23"><component :is="step.icon" /></el-icon></div>
          <h3>{{ step.title }}</h3>
          <p>{{ step.description }}</p>
        </div>
      </div>
    </section>
  </div>
</template>
