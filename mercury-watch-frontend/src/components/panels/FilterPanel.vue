<template>
  <section class="section-card filter-panel">
    <h3>筛选器</h3>
    <el-form label-position="top" size="small">
      <el-form-item label="大洲">
        <el-segmented v-model="continent" :options="continentOptions" />
      </el-form-item>

      <el-form-item label="国家">
        <el-input v-model="iso" placeholder="ISO代码，例如 CN" />
      </el-form-item>

      <el-form-item label="物种">
        <el-input v-model="species" placeholder="学名或通用名" />
      </el-form-item>

      <el-form-item label="水域类型">
        <el-radio-group v-model="freshwaterMarine">
          <el-radio-button value="all">全部</el-radio-button>
          <el-radio-button value="freshwater">淡水</el-radio-button>
          <el-radio-button value="marine">海水</el-radio-button>
        </el-radio-group>
      </el-form-item>

      <el-form-item label="色盲模式">
        <el-radio-group v-model="colorBlindMode">
          <el-radio-button value="none">关闭</el-radio-button>
          <el-radio-button value="protanopia">红色盲</el-radio-button>
          <el-radio-button value="deuteranopia">绿色盲</el-radio-button>
          <el-radio-button value="tritanopia">蓝黄色盲</el-radio-button>
        </el-radio-group>
      </el-form-item>

      <el-form-item :label="`汞浓度上限: ${concentrationMax.toFixed(2)} mg/kg`">
        <el-slider v-model="concentrationMax" :step="0.01" :min="0" :max="2" />
      </el-form-item>

      <div class="stats">
        <el-statistic title="样本数量" :value="sampleCount" />
        <el-statistic title="平均汞浓度" :value="avgConcentration" :precision="3" suffix="mg/kg" />
      </div>

      <el-button type="primary" plain @click="reset">重置筛选</el-button>
    </el-form>
  </section>
</template>

<script setup lang="ts">
import { computed, watch } from "vue";
import { storeToRefs } from "pinia";
import { useFilterStore } from "../../stores/filterStore";
import { useDataStore } from "../../stores/dataStore";
import { useUserStore } from "../../stores/userStore";

const filterStore = useFilterStore();
const dataStore = useDataStore();
const userStore = useUserStore();

const continentOptions = [
  { label: "全部", value: "" },
  { label: "亚洲", value: "Asia" },
  { label: "欧洲", value: "Europe" },
  { label: "非洲", value: "Africa" },
  { label: "北美", value: "North America" },
  { label: "南美", value: "South America" },
  { label: "大洋洲", value: "Oceania" }
];

const { sampleCount, avgConcentration } = storeToRefs(dataStore);
const continent = computed({
  get: () => filterStore.continent,
  set: (value) => filterStore.setFilters({ continent: value })
});
const iso = computed({
  get: () => filterStore.iso,
  set: (value) => filterStore.setFilters({ iso: value })
});
const species = computed({
  get: () => filterStore.species,
  set: (value) => filterStore.setFilters({ species: value })
});
const freshwaterMarine = computed({
  get: () => filterStore.freshwaterMarine,
  set: (value) => filterStore.setFilters({ freshwaterMarine: value })
});
const concentrationMax = computed({
  get: () => filterStore.concentrationMax,
  set: (value) => filterStore.setFilters({ concentrationMax: value })
});
const colorBlindMode = computed({
  get: () => userStore.colorBlindMode,
  set: (value: "none" | "protanopia" | "deuteranopia" | "tritanopia") =>
    userStore.setColorBlindMode(value)
});

watch(
  () => filterStore.getQueryParams(),
  async () => {
    await dataStore.fetchData();
  },
  { deep: true }
);

const reset = async () => {
  filterStore.resetFilters();
  await dataStore.fetchData();
};
</script>

<style scoped>
.filter-panel {
  padding: 14px;
  height: 100%;
}

h3 {
  margin: 0 0 10px;
}

.stats {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
  margin: 10px 0 14px;
}
</style>
