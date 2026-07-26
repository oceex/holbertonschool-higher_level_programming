#!/usr/bin/python3
"""A simple Flask API demonstrating routing, JSON responses,
dynamic routes, and POST request handling.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users, keyed by username
users = {}


@app.route("/")
def home():
    """Root endpoint - welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Return a JSON list of all usernames stored in the API."""
    return jsonify(sorted(users.keys()))


@app.route("/status")
def status():
    """Return a simple OK status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Return the full object corresponding to the provided username."""
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user to the users dictionary from a JSON request body."""
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()