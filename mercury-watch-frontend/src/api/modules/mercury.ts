import request from "../request";

export const getMercuryByRegion = (params: Record<string, unknown>) =>
  request.get("/mercury/by-region", { params });

export const compareSpecies = (payload: Record<string, unknown>) =>
  request.post("/mercury/compare", payload);
