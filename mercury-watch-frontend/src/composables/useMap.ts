export function useMap() {
  const getMarkerStyle = (concentration: number) => {
    const radius = Math.max(6, Math.min(28, concentration * 35));
    const opacity = Math.max(0.35, Math.min(0.9, concentration * 0.9));
    return { radius, opacity };
  };

  return { getMarkerStyle };
}
