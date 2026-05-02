import { defineStore } from "pinia";

export const useCompareStore = defineStore("compare", {
  state: () => ({
    ids: [] as number[]
  }),
  actions: {
    addToCompare(id: number) {
      if (this.ids.includes(id) || this.ids.length >= 4) return;
      this.ids.push(id);
    },
    removeFromCompare(id: number) {
      this.ids = this.ids.filter((item) => item !== id);
    },
    clearCompare() {
      this.ids = [];
    }
  }
});
