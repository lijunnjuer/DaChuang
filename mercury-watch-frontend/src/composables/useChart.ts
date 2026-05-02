export function useChart() {
  const buildBarOption = (title: string, x: string[], y: number[]) => ({
    title: { text: title },
    tooltip: {},
    xAxis: { type: "category", data: x, axisLabel: { interval: 0, rotate: 20 } },
    yAxis: { type: "value" },
    series: [{ type: "bar", data: y, itemStyle: { color: "#1890ff" } }]
  });

  return { buildBarOption };
}
