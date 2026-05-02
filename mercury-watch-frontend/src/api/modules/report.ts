import request from "../request";

export const generateReport = (payload: Record<string, unknown>) =>
  request.post("/report/generate", payload);

export const getReportStatus = (taskId: string) => request.get(`/report/status/${taskId}`);
