<template>
  <main class="page-shell home-page">
    <Header />

    <section class="content-grid">
      <aside class="left section-card">
        <FilterPanel />
      </aside>

      <el-button class="mobile-filter-btn" type="primary" @click="drawerVisible = true">
        打开筛选器
      </el-button>

      <el-drawer v-model="drawerVisible" title="筛选器" direction="ltr" size="82%">
        <FilterPanel />
      </el-drawer>

      <section class="right">
        <el-tabs v-model="activeTab" type="card">
          <el-tab-pane label="地图" name="map">
            <div class="map-layout">
              <MercuryMap :visible="activeTab === 'map'" />
              <div class="map-side">
                <DetailPanel />
                <MapLegend />
                <TimelineSlider />
              </div>
            </div>
          </el-tab-pane>

          <el-tab-pane label="图表" name="charts">
            <div class="charts-layout" v-if="activeTab === 'charts'">
              <BarChart />
              <PieChart />
              <DataTable />
              <ComparePanel />
              <ReportGenerator />
            </div>
          </el-tab-pane>
        </el-tabs>
      </section>
    </section>

    <Footer />
  </main>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import Header from "../components/common/Header.vue";
import Footer from "../components/common/Footer.vue";
import FilterPanel from "../components/panels/FilterPanel.vue";
import MercuryMap from "../components/map/MercuryMap.vue";
import MapLegend from "../components/map/MapLegend.vue";
import TimelineSlider from "../components/map/TimelineSlider.vue";
import DetailPanel from "../components/panels/DetailPanel.vue";
import BarChart from "../components/charts/BarChart.vue";
import PieChart from "../components/charts/PieChart.vue";
import DataTable from "../components/panels/DataTable.vue";
import ComparePanel from "../components/panels/ComparePanel.vue";
import ReportGenerator from "../components/report/ReportGenerator.vue";
import { useDataStore } from "../stores/dataStore";

const activeTab = ref("map");
const drawerVisible = ref(false);
const dataStore = useDataStore();

onMounted(async () => {
  await dataStore.fetchData();
});
</script>

<style scoped>
.home-page {
  display: flex;
  flex-direction: column;
}

.content-grid {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 12px;
}

.left {
  min-height: 760px;
}

.mobile-filter-btn {
  display: none;
}

.right {
  min-width: 0;
}

.map-layout {
  display: grid;
  grid-template-columns: 1fr 300px;
  gap: 12px;
}

.map-side {
  display: grid;
  gap: 12px;
  align-content: start;
}

.charts-layout {
  display: grid;
  gap: 12px;
}

h3 {
  margin: 0;
}

.hint {
  margin-top: 8px;
  color: var(--text-sub);
  font-size: 12px;
}

@media (max-width: 1100px) {
  .content-grid {
    grid-template-columns: 280px 1fr;
  }
}

@media (max-width: 768px) {
  .content-grid {
    grid-template-columns: 1fr;
  }

  .map-layout {
    grid-template-columns: 1fr;
  }

  .left {
    min-height: auto;
    display: none;
  }

  .mobile-filter-btn {
    display: inline-flex;
    width: 140px;
    margin-bottom: 8px;
  }
}
</style>
