export interface MercurySample {
  id: number;
  latitude: number;
  longitude: number;
  continent: string;
  iso: string;
  commonName: string;
  scientificName: string;
  concentration: number;
  freshwaterMarine: "freshwater" | "marine";
  tl: string;
  bodyLengthCm?: number;
}

export interface FilterState {
  continent: string;
  iso: string;
  species: string;
  freshwaterMarine: "all" | "freshwater" | "marine";
  concentrationMax: number;
}
