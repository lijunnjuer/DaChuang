<template>
  <section class="section-card chart-wrap">
    <div ref="chartRef" class="chart"></div>
  </section>
</template>

<script setup lang="ts">
import { nextTick, onBeforeUnmount, onMounted, ref } from "vue";
import * as echarts from "echarts";

const chartRef = ref<HTMLDivElement | null>(null);
let chart: echarts.ECharts | null = null;
let resizeObserver: ResizeObserver | null = null;

const renderChart = async () => {
  await nextTick();
  if (!chartRef.value) return;
  if (!chart) chart = echarts.init(chartRef.value);
  chart.setOption({
    title: { text: "淡水 vs 海水 汞浓度对比" },
    tooltip: {},
    xAxis: { type: "category", data: ["淡水", "海水"] },
    yAxis: { type: "value" },
    series: [
      {
        type: "bar",
        barWidth: 48,
        data: [0.18, 0.31],
        itemStyle: {
          color: (params: { dataIndex: number }) =>
            params.dataIndex === 0 ? "#2a9d8f" : "#e76f51"
        }
      }
    ]
  });
  chart.resize();
};

onMounted(() => {
  renderChart();
  if (chartRef.value && "ResizeObserver" in window) {
    resizeObserver = new ResizeObserver(() => chart?.resize());
    resizeObserver.observe(chartRef.value);
  }
  window.addEventListener("resize", renderChart);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", renderChart);
  resizeObserver?.disconnect();
  chart?.dispose();
  chart = null;
});
</script>

<style scoped>
.chart-wrap {
  padding: 8px;
}

.chart {
  width: 100%;
  height: 320px;
}
</style>
