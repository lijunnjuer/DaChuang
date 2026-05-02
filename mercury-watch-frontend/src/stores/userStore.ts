import { defineStore } from "pinia";

export const useUserStore = defineStore("user", {
  state: () => ({
    profile: null as null | { name: string },
    subscriptions: [] as string[],
    colorBlindMode: "none" as "none" | "protanopia" | "deuteranopia" | "tritanopia"
  }),
  actions: {
    login(name: string) {
      this.profile = { name };
    },
    logout() {
      this.profile = null;
    },
    setColorBlindMode(mode: "none" | "protanopia" | "deuteranopia" | "tritanopia") {
      this.colorBlindMode = mode;
      document.body.classList.remove(
        "color-blind-protanopia",
        "color-blind-deuteranopia",
        "color-blind-tritanopia"
      );
      if (mode !== "none") {
        document.body.classList.add(`color-blind-${mode}`);
      }
    }
  }
});
