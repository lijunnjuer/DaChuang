import { useUserStore } from "../stores/userStore";

export function useColorBlind() {
  const store = useUserStore();
  const toggleMode = (mode: "none" | "protanopia" | "deuteranopia" | "tritanopia") => {
    store.setColorBlindMode(mode);
  };

  return { toggleMode };
}
