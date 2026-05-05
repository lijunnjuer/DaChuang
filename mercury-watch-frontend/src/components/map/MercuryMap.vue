<template>
  <section class="section-card map-wrap">
    <div ref="mapRef" class="map-box"></div>
  </section>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref, watch } from "vue";
import { storeToRefs } from "pinia";
import L from "leaflet";
import { useDataStore } from "../../stores/dataStore";
import { useMapStore } from "../../stores/mapStore";
import { riskColor } from "../../utils/color";

const props = withDefaults(
  defineProps<{
    visible?: boolean;
  }>(),
  {
    visible: false
  }
);

const mapRef = ref<HTMLDivElement | null>(null);
let map: L.Map | null = null;
let layer: L.LayerGroup | null = null;
let complianceLayer: L.GeoJSON | null = null;

const dataStore = useDataStore();
const mapStore = useMapStore();
const { rawData } = storeToRefs(dataStore);

const invalidateMapSize = () => {
  if (!map) return;
  window.setTimeout(() => map?.invalidateSize(), 60);
};

const selectedIds = () => mapStore.selectedPointIds ?? [];

const selectNearestPoint = (lat: number, lng: number) => {
  if (!rawData.value.length) return;
  let nearestId = rawData.value[0].id;
  let nearestDist = Number.POSITIVE_INFINITY;

  rawData.value.forEach((item) => {
    const dLat = item.latitude - lat;
    const dLng = item.longitude - lng;
    const dist = dLat * dLat + dLng * dLng;
    if (dist < nearestDist) {
      nearestDist = dist;
      nearestId = item.id;
    }
  });

  mapStore.togglePointSelection(nearestId);
};

const loadComplianceLayer = async () => {
  if (!map) return;

  try {
    const response = await fetch("/china-compliance-overlay.geojson");
    const geojson = await response.json();

    complianceLayer = L.geoJSON(geojson, {
      style: (feature) => {
        const kind = feature?.properties?.kind;

        if (kind === "nanhai") {
          return {
            color: "#c1121f",
            weight: 2,
            dashArray: "8 6",
            fillOpacity: 0   // 不遮挡底图
          };
        }

        if (kind === "taiwan") {
          return {
            color: "#a4133c",
            weight: 2,
            fillColor: "#ffd6e0",
            fillOpacity: 0.2
          };
        }

        return {
          color: "#24577a",
          weight: 1.5,
          fillColor: "#e6f0f7",
          fillOpacity: 0.05  // 降低透明度
        };
      },
      onEachFeature: (feature, featureLayer) => {
        const name = feature.properties?.name;
        if (name) {
          featureLayer.bindTooltip(name, {
            permanent: true,
            direction: "center",
            className: "map-label"
          });
        }
      }
    });

    complianceLayer.addTo(map);

    //关键：放到底层，不遮挡地图
    complianceLayer.bringToBack();

  } catch {
    console.warn("GeoJSON 加载失败");
  }
};

const addOfficialBaseLayers = () => {
  if (!map) return;

  const token = "51ce881b8940b9d4c6d8acd3ca2d8085";

  const vec = L.tileLayer(
    `https://t{s}.tianditu.gov.cn/DataServer?T=vec_w&x={x}&y={y}&l={z}&tk=${token}`,
    {
      subdomains: ["0","1","2","3","4","5","6","7"],
      maxZoom: 18
    }
  );

  const cva = L.tileLayer(
    `https://t{s}.tianditu.gov.cn/DataServer?T=cva_w&x={x}&y={y}&l={z}&tk=${token}`,
    {
      subdomains: ["0","1","2","3","4","5","6","7"],
      maxZoom: 18
    }
  );

  vec.addTo(map);
  cva.addTo(map);

  //确保底图在最底层
  vec.setZIndex(1);
  cva.setZIndex(2);
};

const paint = () => {
  if (!map) return;

  if (layer) layer.remove();
  layer = L.layerGroup();

  rawData.value.forEach((item) => {
    const radius = Math.max(6, Math.min(20, item.concentration * 35));
    const isSelected = selectedIds().includes(item.id);

    const marker = L.circleMarker([item.latitude, item.longitude], {
      radius: isSelected ? radius + 3 : radius,
      color: riskColor(item.concentration),
      fillColor: riskColor(item.concentration),
      fillOpacity: isSelected ? 0.85 : 0.55,
      weight: isSelected ? 3 : 1
    });

    marker.bindPopup(
      `<b>${item.commonName}</b><br/>MeHg: ${item.concentration} mg/kg<br/>水域: ${item.freshwaterMarine}<br/>国家: ${item.iso}<br/>TL: ${item.tl}<br/>体长: ${item.bodyLengthCm ?? "-"} cm`
    );

    marker.on("click", () => mapStore.togglePointSelection(item.id));
    layer?.addLayer(marker);
  });

  layer.addTo(map);
};

onMounted(() => {
  if (!mapRef.value) return;

  map = L.map(mapRef.value, {
    zoomControl: true,
    worldCopyJump: true
  }).setView(mapStore.center, mapStore.zoom);

  addOfficialBaseLayers();
  loadComplianceLayer();

  map.on("click", (e: L.LeafletMouseEvent) => {
    selectNearestPoint(e.latlng.lat, e.latlng.lng);
  });

  paint();
  invalidateMapSize();

  window.addEventListener("resize", invalidateMapSize);
});

onBeforeUnmount(() => {
  window.removeEventListener("resize", invalidateMapSize);
});

watch(rawData, () => paint(), { deep: true });

watch(
  () => mapStore.selectedPointIds,
  () => paint(),
  { deep: true }
);

watch(
  () => props.visible,
  (visible) => {
    if (visible) invalidateMapSize();
  },
  { immediate: true }
);
</script>

<style scoped>
.map-wrap {
  height: 520px;
  padding: 8px;
}

.map-box {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  overflow: hidden;
  background: #dfeaf5;
}

:global(.map-label) {
  background: rgba(255, 255, 255, 0.88);
  border: 1px solid #bcd0e2;
  color: #20445d;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 11px;
  font-weight: 600;
}
</style>
