<template>
  <section class="section-card report-box">
    <h3>报告生成</h3>
    <p>当前提供按钮占位，后续可接入异步任务轮询和下载链接。</p>
    <el-button type="primary" @click="onGenerate">生成PDF报告</el-button>
  </section>
</template>

<script setup lang="ts">
import { useReportStore } from "../../stores/reportStore";

const reportStore = useReportStore();
const onGenerate = async () => {
  await reportStore.generateReport();
};
</script>

<style scoped>
.report-box {
  padding: 12px;
}

h3 {
  margin: 0 0 8px;
}
</style>
