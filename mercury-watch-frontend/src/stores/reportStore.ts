import { defineStore } from "pinia";

export const useReportStore = defineStore("report", {
  state: () => ({
    taskId: "",
    status: "idle" as "idle" | "pending" | "completed" | "failed",
    downloadUrl: ""
  }),
  actions: {
    async generateReport() {
      this.status = "pending";
    },
    async pollStatus() {
      if (this.status === "pending") this.status = "completed";
    },
    downloadReport() {
      return this.downloadUrl;
    }
  }
});
