import { ref } from "vue";

export function useDebounce(delay = 300) {
  const timer = ref<number | undefined>();
  const run = (fn: () => void) => {
    window.clearTimeout(timer.value);
    timer.value = window.setTimeout(fn, delay);
  };
  return { run };
}
