from flask import Flask, request, jsonify
from flask_cors import CORS
import requests # Used to make HTTP requests to JSONPlaceholder

app = Flask(__name__)
CORS(app) # Enable CORS (Cross-Origin Resource Sharing) for your frontend

# JSONPlaceholder base URL
JSONPLACEHOLDER_BASE_URL = "https://jsonplaceholder.typicode.com"

@app.route('/')
def hello_world():
    return "Backend for JSONPlaceholder is running!"

@app.route('/api/get_posts', methods=['GET'])
def get_posts():
    """Fetches a list of posts from JSONPlaceholder."""
    try:
        response = requests.get(f"{JSONPLACEHOLDER_BASE_URL}/posts?_limit=5") # Get first 5 posts
        response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
        posts = response.json()
        return jsonify({"success": True, "data": posts})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/get_comments', methods=['GET'])
def get_comments():
    """Fetches a list of comments from JSONPlaceholder."""
    try:
        response = requests.get(f"{JSONPLACEHOLDER_BASE_URL}/comments?_limit=5") # Get first 5 comments
        response.raise_for_status()
        comments = response.json()
        return jsonify({"success": True, "data": comments})
    except requests.exceptions.RequestException as e:
        print(f"Error fetching comments: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

@app.route('/api/create_post', methods=['POST'])
def create_post():
    """Creates a new post on JSONPlaceholder (simulated)."""
    data = request.get_json() # Get the JSON data sent from the frontend
    if not data or 'title' not in data or 'body' not in data:
        return jsonify({"success": False, "message": "Title and body are required"}), 400

    # JSONPlaceholder uses a fake POST request. It will return the new object
    # but won't actually store it. This is perfect for a demo!
    try:
        response = requests.post(f"{JSONPLACEHOLDER_BASE_URL}/posts", json=data)
        response.raise_for_status()
        new_post = response.json()
        return jsonify({"success": True, "message": "Post created successfully", "data": new_post}), 201
    except requests.exceptions.RequestException as e:
        print(f"Error creating post: {e}")
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    # When running locally, use debug mode
    app.run(debug=True, port=5000)
