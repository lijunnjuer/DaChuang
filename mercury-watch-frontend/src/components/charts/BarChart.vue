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
    title: { text: "物种平均汞含量前12名" },
    tooltip: {},
    xAxis: {
      type: "category",
      axisLabel: { interval: 0, rotate: 30 },
      data: ["金枪鱼", "鲨鱼", "旗鱼", "带鱼", "鲈鱼", "黄鱼", "鲶鱼", "鲤鱼", "鲫鱼", "罗非鱼", "鳕鱼", "鲭鱼"]
    },
    yAxis: { type: "value" },
    series: [{
      type: "bar",
      data: [0.52, 0.48, 0.44, 0.36, 0.31, 0.28, 0.22, 0.18, 0.15, 0.11, 0.1, 0.09],
      itemStyle: { color: "#1f78b4" }
    }]
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
