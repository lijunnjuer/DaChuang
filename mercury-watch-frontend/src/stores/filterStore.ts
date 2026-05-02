import { defineStore } from "pinia";
import type { FilterState } from "../types";

const initialState: FilterState = {
  continent: "",
  iso: "",
  species: "",
  freshwaterMarine: "all",
  concentrationMax: 2.0
};

export const useFilterStore = defineStore("filter", {
  state: (): FilterState => ({ ...initialState }),
  actions: {
    setFilters(payload: Partial<FilterState>) {
      Object.assign(this, payload);
    },
    resetFilters() {
      Object.assign(this, initialState);
    },
    getQueryParams() {
      return { ...this };
    }
  }
});
