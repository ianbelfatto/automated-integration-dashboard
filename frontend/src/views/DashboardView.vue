<template>
  <div class="dashboard-container">
    <header class="dashboard-header">
      <h1>Content Management Dashboard</h1>
      <p>Manage your posts and comments effectively.</p>
    </header>

    <main class="dashboard-main">
      <section class="integration-section">
        <h2>Content Feeds</h2>
        <div class="cards-grid">
          <IntegrationCard
            ref="postsCard"
            title="Recent Posts"
            api-endpoint="/api/get_posts"
          />
          <IntegrationCard
            title="Recent Comments"
            api-endpoint="/api/get_comments"
          />
        </div>
      </section>

      <section class="automation-section">
        <h2>Automated Content Creation</h2>
        <AutomationForm @post-created="handlePostCreated" />
      </section>

      <section class="logs-section">
        <h2>Activity Logs</h2>
        <div class="log-area">
          <p
            v-for="(log, index) in activityLogs"
            :key="index"
            :class="log.type === 'success' ? 'log-success' : 'log-info'"
          >
            {{ log.message }}
          </p>
          <p v-if="activityLogs.length === 0" class="log-info">
            No activity yet. Try creating a post!
          </p>
        </div>
      </section>
    </main>
  </div>
</template>

<script>
import IntegrationCard from "@/components/IntegrationCard.vue";
import AutomationForm from "@/components/AutomationForm.vue";

export default {
  name: "DashboardView",
  components: {
    IntegrationCard,
    AutomationForm,
  },
  data() {
    return {
      activityLogs: [],
    };
  },
  methods: {
    handlePostCreated() {
      // Refresh the posts IntegrationCard when a new post is created
      this.$refs.postsCard.fetchData();
      this.addLog("New post published! (simulated)", "success");
    },
    addLog(message, type = "info") {
      this.activityLogs.unshift({ message, type, timestamp: new Date() });
      if (this.activityLogs.length > 10) {
        // Keep logs concise
        this.activityLogs.pop();
      }
    },
  },
  mounted() {
    this.addLog("Dashboard loaded.", "info");
  },
};
</script>

<style scoped>
.dashboard-container {
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f4f7f6;
  min-height: 100vh;
  padding: 20px;
  color: #333;
}

.dashboard-header {
  text-align: center;
  margin-bottom: 30px;
  padding: 20px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
}

.dashboard-header h1 {
  color: #2c3e50;
  margin-bottom: 10px;
}

.dashboard-main {
  display: grid;
  grid-template-columns: 1fr;
  gap: 30px;
  max-width: 1200px;
  margin: 0 auto;
}

@media (min-width: 768px) {
  .dashboard-main {
    grid-template-columns: 2fr 1fr; /* Two columns on larger screens */
  }
  .integration-section {
    grid-column: span 2; /* Integrations span both columns */
  }
}

.section {
  background-color: #fff;
  padding: 25px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.05);
}

.section h2 {
  color: #4a69bd;
  margin-top: 0;
  margin-bottom: 20px;
  border-bottom: 1px solid #eee;
  padding-bottom: 10px;
}

.cards-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

@media (min-width: 600px) {
  .cards-grid {
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  }
}

.log-area {
  background-color: #f0f4f7;
  border: 1px solid #e0e0e0;
  border-radius: 5px;
  padding: 15px;
  min-height: 100px;
  max-height: 250px;
  overflow-y: auto;
}

.log-info {
  color: #555;
  font-size: 0.9em;
  margin-bottom: 5px;
}

.log-success {
  color: #28a745;
  font-weight: bold;
  font-size: 0.9em;
  margin-bottom: 5px;
}

/* Base styles for AutomationForm and IntegrationCard are scoped within their components */
</style>
