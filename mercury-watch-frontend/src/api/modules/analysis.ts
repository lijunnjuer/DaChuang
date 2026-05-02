import request from "../request";

export const getTopSpecies = () => request.get("/analysis/top-species");
export const getWaterComparison = () => request.get("/analysis/water-comparison");
