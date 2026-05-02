import request from "../request";

export const getSpeciesList = () => request.get("/species");
export const getSpeciesDetail = (id: number) => request.get(`/species/${id}`);
export const searchSpecies = (keyword: string) => request.get("/species/search", { params: { keyword } });
