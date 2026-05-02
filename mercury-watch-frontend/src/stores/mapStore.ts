import { defineStore } from "pinia";

export const useMapStore = defineStore("map", {
  state: () => ({
    zoom: 2,
    center: [20, 110] as [number, number],
    selectedPointIds: [] as number[],
    aggregationMode: "region" as "grid" | "region" | "cluster" | "raw"
  }),
  actions: {
    setZoom(zoom: number) {
      this.zoom = zoom;
    },
    setCenter(center: [number, number]) {
      this.center = center;
    },
    togglePointSelection(id: number) {
      if (this.selectedPointIds.includes(id)) {
        this.selectedPointIds = this.selectedPointIds.filter((item) => item !== id);
      } else {
        this.selectedPointIds.push(id);
      }
    },
    clearSelectedPoints() {
      this.selectedPointIds = [];
    },
    setAggregationMode(mode: "grid" | "region" | "cluster" | "raw") {
      this.aggregationMode = mode;
    }
  }
});
