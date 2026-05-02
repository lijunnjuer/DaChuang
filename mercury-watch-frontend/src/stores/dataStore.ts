import { defineStore } from "pinia";
import type { MercurySample } from "../types";

const mockSamples: MercurySample[] = [
  {
    id: 1,
    latitude: 31.2,
    longitude: 121.5,
    continent: "Asia",
    iso: "CN",
    commonName: "金枪鱼",
    scientificName: "Thunnus thynnus",
    concentration: 0.42,
    freshwaterMarine: "marine",
    tl: "TL_5",
    bodyLengthCm: 152
  },
  {
    id: 2,
    latitude: 30.6,
    longitude: 114.3,
    continent: "Asia",
    iso: "CN",
    commonName: "鲈鱼",
    scientificName: "Lateolabrax japonicus",
    concentration: 0.17,
    freshwaterMarine: "freshwater",
    tl: "TL_4",
    bodyLengthCm: 48
  },
  {
    id: 3,
    latitude: 23.1,
    longitude: 113.2,
    continent: "Asia",
    iso: "CN",
    commonName: "黄鱼",
    scientificName: "Larimichthys crocea",
    concentration: 0.28,
    freshwaterMarine: "marine",
    tl: "TL_4",
    bodyLengthCm: 36
  },
  {
    id: 4,
    latitude: 35.7,
    longitude: 139.7,
    continent: "Asia",
    iso: "JP",
    commonName: "鲭鱼",
    scientificName: "Scomber japonicus",
    concentration: 0.21,
    freshwaterMarine: "marine",
    tl: "TL_4",
    bodyLengthCm: 42
  },
  {
    id: 5,
    latitude: 37.8,
    longitude: -122.4,
    continent: "North America",
    iso: "US",
    commonName: "鲑鱼",
    scientificName: "Oncorhynchus",
    concentration: 0.11,
    freshwaterMarine: "freshwater",
    tl: "TL_3",
    bodyLengthCm: 63
  }
];

export const useDataStore = defineStore("data", {
  state: () => ({
    rawData: [] as MercurySample[],
    loading: false,
    etagCache: new Map<string, string>()
  }),
  getters: {
    sampleCount: (state) => state.rawData.length,
    avgConcentration: (state) => {
      if (!state.rawData.length) return 0;
      const total = state.rawData.reduce((sum, item) => sum + item.concentration, 0);
      return Number((total / state.rawData.length).toFixed(3));
    }
  },
  actions: {
    async fetchData() {
      this.loading = true;
      this.rawData = mockSamples;
      this.loading = false;
    },
    clearCache() {
      this.etagCache.clear();
    }
  }
});
