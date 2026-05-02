<template>
  <section class="section-card legend">
    <h4>风险图例</h4>
    <ul>
      <li><span class="dot low"></span> 低风险 ≤0.1</li>
      <li><span class="dot mid"></span> 中风险 0.2-0.3</li>
      <li><span class="dot high"></span> 高风险 >0.5</li>
    </ul>
    <div class="compliance-note">
      底图优先级: 天地图官方服务 -> 标准地图影像替换；并叠加台湾省、南海断续线合规标识。
    </div>
  </section>
</template>

<style scoped>
.legend {
  padding: 10px;
}

h4 {
  margin: 0 0 8px;
}

ul {
  margin: 0;
  padding: 0;
  list-style: none;
  display: grid;
  gap: 6px;
  font-size: 12px;
}

.dot {
  display: inline-block;
  width: 10px;
  height: 10px;
  border-radius: 99px;
  margin-right: 6px;
}

.low { background: var(--risk-low); }
.mid { background: var(--risk-mid); }
.high { background: var(--risk-high); }

.compliance-note {
  margin-top: 8px;
  padding-top: 8px;
  border-top: 1px dashed var(--line);
  font-size: 11px;
  color: var(--text-sub);
  line-height: 1.4;
}
</style>
