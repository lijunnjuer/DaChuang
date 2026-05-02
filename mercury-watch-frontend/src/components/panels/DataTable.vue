<template>
  <section class="section-card table-wrap">
    <h3>数据详情表</h3>
    <el-table :data="rows" size="small" height="260">
      <el-table-column prop="commonName" label="物种" min-width="120" />
      <el-table-column prop="concentration" label="MeHg (mg/kg)" min-width="120" />
      <el-table-column prop="freshwaterMarine" label="水域" min-width="100" />
      <el-table-column prop="iso" label="国家" min-width="90" />
      <el-table-column prop="tl" label="TL" min-width="80" />
    </el-table>
  </section>
</template>

<script setup lang="ts">
import { storeToRefs } from "pinia";
import { useDataStore } from "../../stores/dataStore";

const store = useDataStore();
const { rawData: rows } = storeToRefs(store);
</script>

<style scoped>
.table-wrap {
  padding: 12px;
}

h3 {
  margin: 0 0 10px;
}
</style>
