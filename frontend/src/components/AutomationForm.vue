<template>
  <div class="automation-form">
    <h4>Create New Blog Post</h4>
    <form @submit.prevent="createPost">
      <input
        type="text"
        v-model="title"
        placeholder="Post Title"
        required
        class="input-field"
      />
      <textarea
        v-model="body"
        placeholder="Post Content"
        required
        class="textarea-field"
      ></textarea>
      <button type="submit" :disabled="submitting" class="submit-button">
        {{ submitting ? "Creating Post..." : "Publish Post" }}
      </button>
    </form>
    <p
      v-if="message"
      :class="{ 'success-message': isSuccess, 'error-message': !isSuccess }"
    >
      {{ message }}
    </p>
  </div>
</template>

<script>
export default {
  name: "AutomationForm",
  data() {
    return {
      title: "",
      body: "",
      submitting: false,
      message: "",
      isSuccess: false,
    };
  },
  methods: {
    async createPost() {
      this.submitting = true;
      this.message = "";
      this.isSuccess = false;
      try {
        const response = await fetch("https://my-dashboard-backend-3qdq.onrender.com/api/create_post", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            title: this.title,
            body: this.body,
            userId: 1,
          }), // userId is required by JSONPlaceholder
        });

        const data = await response.json();
        if (data.success) {
          this.message = data.message;
          this.isSuccess = true;
          this.title = "";
          this.body = "";
          // Emit an event to tell the parent (DashboardView) to refresh the posts list
          this.$emit("post-created");
        } else {
          this.message = `Error: ${data.message}`;
          this.isSuccess = false;
        }
      } catch (e) {
        this.message = `Network error: ${e.message}`;
        this.isSuccess = false;
        console.error("Automation error:", e);
      } finally {
        this.submitting = false;
      }
    },
  },
};
</script>

<style scoped>
.automation-form {
  border: 1px solid #e0e0e0;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
  background-color: #fff;
}
h4 {
  color: #333;
  margin-top: 0;
}
.input-field,
.textarea-field {
  display: block;
  margin-bottom: 10px;
  padding: 10px;
  width: calc(100% - 20px);
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 1rem;
}
.textarea-field {
  min-height: 80px;
  resize: vertical;
}
.submit-button {
  background-color: #28a745;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1rem;
}
.submit-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
.submit-button:hover:not(:disabled) {
  background-color: #218838;
}
.success-message {
  color: green;
  margin-top: 10px;
}
.error-message {
  color: red;
  margin-top: 10px;
}
</style>
