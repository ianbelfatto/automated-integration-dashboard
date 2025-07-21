import { createRouter, createWebHistory } from "vue-router";
import DashboardView from "../views/DashboardView.vue"; // Correct path to your view

const routes = [
  {
    path: "/",
    name: "dashboard",
    component: DashboardView,
  },
  // Add other routes if your app grows (e.g., /settings)
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
