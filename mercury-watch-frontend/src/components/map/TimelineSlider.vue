<template>
  <section class="section-card timeline">
    <div class="label">年份区间（扩展功能预留）</div>
    <el-slider range :min="2000" :max="2026" :model-value="[2020, 2024]" />
  </section>
</template>

<style scoped>
.timeline {
  padding: 10px;
}

.label {
  font-size: 12px;
  color: var(--text-sub);
  margin-bottom: 4px;
}
</style>
