<template>
  <div class="integration-card">
    <h3>{{ title }}</h3>
    <p v-if="loading">Loading...</p>
    <p v-else-if="error" class="error-message">{{ error }}</p>
    <ul v-else>
      <li v-for="item in items" :key="item.id">
        <strong>{{ item.title || item.name }}</strong
        ><br />
        <small>{{ item.body || item.email }}</small>
      </li>
    </ul>
    <button @click="fetchData">Refresh Data</button>
  </div>
</template>

<script>
export default {
  name: "IntegrationCard",
  props: {
    title: String, // e.g., "Recent Posts" or "Recent Comments"
    apiEndpoint: String, // e.g., "/api/get_posts" or "/api/get_comments"
  },
  data() {
    return {
      items: [],
      loading: false,
      error: null,
    };
  },
  methods: {
    async fetchData() {
      this.loading = true;
      this.error = null;
      try {
        const response = await fetch(
          `http://127.0.0.1:5000${this.apiEndpoint}`
        );
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        const data = await response.json();
        if (data.success) {
          this.items = data.data;
        } else {
          this.error = data.message || "Failed to fetch data";
        }
      } catch (e) {
        this.error = `Error fetching data: ${e.message}`;
        console.error("Fetch error:", e);
      } finally {
        this.loading = false;
      }
    },
  },
  mounted() {
    this.fetchData(); // Fetch data when the component is mounted
  },
};
</script>

<style scoped>
.integration-card {
  border: 1px solid #e0e0e0;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  background-color: #fff;
}
h3 {
  color: #333;
  margin-top: 0;
}
ul {
  list-style-type: none;
  padding: 0;
  max-height: 250px; /* Limit height for scrollbar if many items */
  overflow-y: auto;
  border-top: 1px solid #eee;
  padding-top: 10px;
}
li {
  background: #fdfdfd;
  margin-bottom: 8px;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #f0f0f0;
}
button {
  background-color: #007bff;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 10px;
}
button:hover {
  background-color: #0056b3;
}
.error-message {
  color: red;
}
</style>
