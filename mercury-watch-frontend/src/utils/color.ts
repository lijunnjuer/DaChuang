export function riskColor(value: number) {
  if (value <= 0.1) return "var(--risk-low)";
  if (value <= 0.2) return "var(--risk-mid-low)";
  if (value <= 0.3) return "var(--risk-mid)";
  if (value <= 0.5) return "var(--risk-mid-high)";
  return "var(--risk-high)";
}
