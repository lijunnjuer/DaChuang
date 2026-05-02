# 产品汞含量风险地图系统脚手架

本目录包含两个子项目：

- `mercury-watch-frontend`：Vue 3 + TypeScript 前端框架
- `mercury-watch-backend`：Flask 分层后端框架（仅骨架，无业务逻辑）

## 前端启动

```bash
cd mercury-watch-frontend
npm install
npm run dev
```

## 后端启动

```bash
cd mercury-watch-backend
python -m venv .venv
# Windows
.venv\Scripts\activate
pip install -r requirements.txt
python wsgi.py
```

## Docker（后端）

```bash
cd mercury-watch-backend
docker compose up --build
```

## 说明

- 当前实现重点是“结构完整 + 页面框架完整”。
- 已实现首页左右布局、筛选器、地图点位渲染、双图表标签页、统计表与移动端筛选抽屉。
- 后端 API / Service / DAO / Model / Schema 均已建立，可直接进入业务开发阶段。
