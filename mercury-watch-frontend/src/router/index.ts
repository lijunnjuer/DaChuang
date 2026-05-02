import { createRouter, createWebHistory } from "vue-router";

const HomePage = () => import("../views/HomePage.vue");
const AnalysisPage = () => import("../views/AnalysisPage.vue");
const AboutPage = () => import("../views/AboutPage.vue");
const AdminPage = () => import("../views/AdminPage.vue");
const ReportPage = () => import("../views/ReportPage.vue");

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", name: "home", component: HomePage },
    { path: "/analysis", name: "analysis", component: AnalysisPage },
    { path: "/about", name: "about", component: AboutPage },
    { path: "/admin", name: "admin", component: AdminPage },
    { path: "/report/:taskId", name: "report", component: ReportPage }
  ]
});

export default router;
