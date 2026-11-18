<script setup>
import { ref } from 'vue'
import { ArrowLeft, ArrowRight, Calendar, Lock, Message, User } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import logoUrl from '@/assets/icons/logo.svg'

const formRef = ref()
const form = ref({ username: '', email: '', password: '', confirmPassword: '' })
const validateConfirmPassword = (_rule, value, callback) => {
  if (!value) callback(new Error('请再次输入密码'))
  else if (value !== form.value.password) callback(new Error('两次输入的密码不一致'))
  else callback()
}
const rules = {
  username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' },
    { type: 'email', message: '请输入有效的邮箱地址', trigger: ['blur', 'change'] },
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' },
    { min: 8, message: '密码至少需要 8 个字符', trigger: 'blur' },
  ],
  confirmPassword: [{ validator: validateConfirmPassword, trigger: ['blur', 'change'] }],
}

async function handleRegister() {
  if (!formRef.value) return
  try {
    await formRef.value.validate()
    ElMessage.info('注册功能尚未接入服务，请联系管理员配置注册接口。')
  } catch {
    // Element Plus displays validation errors beside the fields.
  }
}
</script>

<template>
  <div class="register-page">
    <section class="register-story" aria-label="SmartLab 介绍">
      <router-link class="register-brand" to="/" aria-label="返回 SmartLab 首页">
        <img :src="logoUrl" alt="" width="44" height="44" />
        <span>Smart<span>Lab</span><small>实验室预约平台</small></span>
      </router-link>
      <div class="story-content">
        <div class="story-eyebrow"><span></span> SPACE FOR DISCOVERY</div>
        <h1>好的开始，<br />从这里发生<span>。</span></h1>
        <p>创建账户，轻松规划你的每一次实验室探索。</p>
        <div class="story-art" aria-hidden="true">
          <div class="story-orbit orbit-a"></div>
          <div class="story-orbit orbit-b"></div>
          <div class="story-orbit orbit-c"></div>
          <div class="story-center"><el-icon :size="48"><Calendar /></el-icon></div>
          <span class="story-spark spark-a">✦</span>
          <span class="story-spark spark-b">✳</span>
        </div>
      </div>
      <div class="story-footer"><span>SMART SPACE · BETTER RESEARCH</span><span>© {{ new Date().getFullYear() }} SmartLab</span></div>
    </section>

    <main class="register-main">
      <router-link class="back-link" to="/"><el-icon><ArrowLeft /></el-icon> 返回首页</router-link>
      <div class="register-form-wrap">
        <div class="mobile-brand"><img :src="logoUrl" alt="" width="40" height="40" />Smart<span>Lab</span></div>
        <div class="form-eyebrow">GET STARTED <span>—</span> 加入 SmartLab</div>
        <h2>创建你的账户</h2>
        <p class="form-description">填写以下信息，开启你的实验室之旅。</p>

        <el-form ref="formRef" :model="form" :rules="rules" label-position="top" class="register-form" @submit.prevent="handleRegister">
          <el-form-item label="账号" prop="username">
            <el-input v-model.trim="form.username" autocomplete="username" placeholder="请输入账号" size="large" clearable>
              <template #prefix><el-icon><User /></el-icon></template>
            </el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model.trim="form.email" type="email" autocomplete="email" placeholder="请输入邮箱地址" size="large" clearable>
              <template #prefix><el-icon><Message /></el-icon></template>
            </el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input v-model="form.password" type="password" autocomplete="new-password" placeholder="至少 8 个字符" size="large" show-password>
              <template #prefix><el-icon><Lock /></el-icon></template>
            </el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="confirmPassword">
            <el-input v-model="form.confirmPassword" type="password" autocomplete="new-password" placeholder="请再次输入密码" size="large" show-password>
              <template #prefix><el-icon><Lock /></el-icon></template>
            </el-input>
          </el-form-item>
          <el-button class="register-submit" native-type="submit" size="large">创建账户 <el-icon><ArrowRight /></el-icon></el-button>
        </el-form>
        <p class="register-hint">已有账户？<router-link to="/login">返回登录</router-link></p>
      </div>
      <div class="register-bottom">安全、便捷地安排每一次实验。</div>
    </main>
  </div>
</template>

<style scoped>
.register-page { min-height: 100vh; min-height: 100svh; display: grid; grid-template-columns: minmax(380px, 48%) 1fr; background: #fff; color: #263e32; }
.register-story { position: relative; display: flex; flex-direction: column; min-height: 100vh; min-height: 100svh; overflow: hidden; padding: 42px clamp(35px, 5.1vw, 82px) 32px; background: #225c46; color: #fff; }
.register-story::before { content: ''; position: absolute; width: 720px; height: 720px; right: -360px; top: 10%; border-radius: 50%; background: radial-gradient(circle, #4a9470 0%, #2e7455 40%, transparent 72%); opacity: .65; pointer-events: none; }
.register-brand { position: relative; z-index: 1; display: inline-flex; align-items: center; align-self: flex-start; gap: 11px; color: #fff; text-decoration: none; }.register-brand > span { font-size: 22px; font-weight: 800; line-height: 1; letter-spacing: -.6px; }.register-brand > span > span { color: #bce4c5; font-weight: inherit; }.register-brand small { display: block; margin-top: 7px; color: #c0dac7; font-size: 10px; font-weight: 500; letter-spacing: 2px; }
.story-content { position: relative; z-index: 1; flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 28px 0; }.story-eyebrow { display: flex; align-items: center; gap: 11px; color: #bbdfc4; font-size: 11px; font-weight: 700; letter-spacing: 2.5px; }.story-eyebrow span { width: 22px; height: 1px; background: currentColor; }.story-content h1 { margin: 22px 0 15px; font-size: clamp(34px, 3.3vw, 52px); font-weight: 750; letter-spacing: -1.2px; line-height: 1.4; }.story-content h1 span { color: #b6e5bd; font-weight: inherit; }.story-content > p { margin: 0; color: #d2e9d7; font-size: 13px; line-height: 1.9; }
.story-art { position: relative; width: min(100%, 460px); height: clamp(150px, 22vh, 220px); margin-top: 26px; }.story-orbit { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-22deg); border: 1px solid #d6f0d64d; border-radius: 45%; }.orbit-a { width: 92%; height: 93%; }.orbit-b { width: 70%; height: 72%; }.orbit-c { width: 48%; height: 50%; }.story-center { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-10deg); display: grid; place-items: center; width: 105px; height: 105px; border-radius: 28px; color: #28694b; background: linear-gradient(145deg, #d6f2d7, #7dbd94); box-shadow: 12px 22px 35px #16483288, inset 4px 5px 13px #ffffff90; }.story-center .el-icon { transform: rotate(10deg); }.story-spark { position: absolute; color: #c5e8c7; }.spark-a { top: 2%; left: 17%; font-size: 24px; }.spark-b { right: 8%; bottom: 12%; font-size: 20px; }.story-footer { position: relative; z-index: 1; display: flex; justify-content: space-between; gap: 12px; color: #a8d1b4; font-size: 10px; letter-spacing: 1px; }
.register-main { min-width: 0; min-height: 100vh; min-height: 100svh; display: flex; flex-direction: column; padding: 36px clamp(30px, 5vw, 80px) 26px; }.back-link { display: inline-flex; align-items: center; align-self: flex-end; gap: 7px; color: #86978a; text-decoration: none; font-size: 12px; transition: color .2s; }.back-link:hover { color: #287a51; }
.register-form-wrap { width: 100%; max-width: 390px; margin: auto; padding: 24px 0; }.mobile-brand { display: none; }.form-eyebrow { color: #4f9a6c; font-size: 10px; font-weight: 700; letter-spacing: 2px; }.form-eyebrow span { margin: 0 5px; color: #b3c7b7; }.register-form-wrap h2 { margin: 12px 0 7px; color: #263e32; font-size: clamp(29px, 3vw, 39px); line-height: 1.35; font-weight: 750; letter-spacing: -.8px; }.form-description { margin: 0 0 25px; color: #94a498; font-size: 13px; }
.register-form :deep(.el-form-item) { margin-bottom: 17px; }.register-form :deep(.el-form-item__label) { margin-bottom: 5px; color: #3a5543; font-size: 13px; font-weight: 650; }.register-form :deep(.el-input__wrapper) { min-height: 48px; padding: 0 15px; border-radius: 9px; box-shadow: 0 0 0 1px #e2ebe3 inset; }.register-form :deep(.el-input__wrapper:hover) { box-shadow: 0 0 0 1px #91bba0 inset; }.register-form :deep(.el-input.is-focus .el-input__wrapper) { box-shadow: 0 0 0 1px #46966a inset; }.register-form :deep(.el-input__prefix) { color: #87a592; }.register-form :deep(.el-input__inner) { font-size: 13px; }
.register-submit.el-button { width: 100%; min-height: 50px; margin-top: 11px; display: flex; align-items: center; gap: 11px; border: 0; border-radius: 9px; background: #2b7854; color: #fff; font-size: 14px; font-weight: 700; transition: background .2s, transform .2s; }.register-submit.el-button:hover { background: #236647; transform: translateY(-1px); }.register-hint { margin: 20px 0 0; color: #a2afa5; font-size: 11px; line-height: 1.8; text-align: center; }.register-hint a { color: #287a51; font-weight: 700; text-decoration: none; }.register-hint a:hover { text-decoration: underline; }.register-bottom { color: #b1bdb3; font-size: 11px; text-align: center; }
@media (max-width: 900px) { .register-page { grid-template-columns: minmax(300px, 42%) 1fr; }.register-story { padding: 34px 30px 26px; }.register-main { padding: 34px 30px 26px; }.story-content h1 { font-size: 32px; }.story-art { height: 170px; } }
@media (max-width: 680px) { .register-page { display: block; }.register-story { display: none; }.register-main { min-height: 100vh; min-height: 100svh; padding: 24px 25px 28px; }.register-form-wrap { padding: 28px 0 35px; }.mobile-brand { display: flex; align-items: center; gap: 8px; margin-bottom: 40px; color: #263e32; font-size: 21px; font-weight: 800; }.mobile-brand span { margin-left: -8px; color: #3b9d72; font-weight: inherit; } }
@media (prefers-reduced-motion: reduce) { .register-submit.el-button { transition: none; } }
</style>
