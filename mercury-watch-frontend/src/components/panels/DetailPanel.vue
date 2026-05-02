<template>
  <section class="section-card panel">
    <h3>详情面板</h3>
    <p v-if="!selectedRows.length" class="empty">点击地图点位后会在这里累积显示，可多选。</p>

    <div v-else class="toolbar">
      <span>已选择 {{ selectedRows.length }} 个点位</span>
      <el-button link type="danger" @click="clearAll">清空</el-button>
    </div>

    <el-scrollbar max-height="280px" v-if="selectedRows.length">
      <div class="item" v-for="row in selectedRows" :key="row.id">
        <div class="title-row">
          <strong>{{ row.commonName }}</strong>
          <el-button link type="primary" @click="removeOne(row.id)">移除</el-button>
        </div>
        <div class="meta">浓度: {{ row.concentration }} mg/kg</div>
        <div class="meta">国家: {{ row.iso }} | 水域: {{ row.freshwaterMarine }} | TL: {{ row.tl }}</div>
        <div class="meta">体长: {{ row.bodyLengthCm ?? "-" }} cm | 坐标: {{ row.latitude }}, {{ row.longitude }}</div>
      </div>
    </el-scrollbar>
  </section>
</template>

<script setup lang="ts">
import { computed } from "vue";
import { storeToRefs } from "pinia";
import { useMapStore } from "../../stores/mapStore";
import { useDataStore } from "../../stores/dataStore";

const mapStore = useMapStore();
const dataStore = useDataStore();
const { rawData } = storeToRefs(dataStore);

const selectedIds = () => mapStore.selectedPointIds ?? [];

const selectedRows = computed(() =>
  rawData.value.filter((item) => selectedIds().includes(item.id))
);

const removeOne = (id: number) => {
  mapStore.togglePointSelection(id);
};

const clearAll = () => {
  mapStore.clearSelectedPoints();
};
</script>

<style scoped>
.panel {
  padding: 12px;
}

.empty {
  margin: 0;
  color: var(--text-sub);
  font-size: 12px;
}

.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
  color: var(--text-sub);
  font-size: 12px;
}

.item {
  padding: 8px;
  border: 1px solid var(--line);
  border-radius: 8px;
  margin-bottom: 8px;
}

.title-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.meta {
  font-size: 12px;
  color: var(--text-sub);
  margin-top: 2px;
}
</style>
