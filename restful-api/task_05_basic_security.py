#!/usr/bin/python3
"""
API Security and Authentication Techniques.

This module implements a small Flask API demonstrating:
    - Basic HTTP Authentication (Flask-HTTPAuth)
    - Token-based Authentication with JSON Web Tokens (Flask-JWT-Extended)
    - Role-based Access Control (RBAC)
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# ---------------------------------------------------------------------------
# In-memory user store
# ---------------------------------------------------------------------------
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ---------------------------------------------------------------------------
# Basic Authentication
# ---------------------------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify a username/password pair against the in-memory user store."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


# ---------------------------------------------------------------------------
# JWT Authentication
# ---------------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """Authenticate a user with username/password and issue a JWT token."""
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    additional_claims = {"role": user["role"]}
    access_token = create_access_token(
        identity=username, additional_claims=additional_claims
    )
    return jsonify(access_token=access_token)


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route protected by a valid JWT token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route protected by a valid JWT token belonging to an admin user."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# ---------------------------------------------------------------------------
# JWT error handlers - always return 401 for auth-related errors
# ---------------------------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle requests missing a JWT token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle requests with a malformed/invalid JWT token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle requests with an expired JWT token."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle requests with a revoked JWT token."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle requests that require a fresh JWT token."""
    return jsonify({"error": "Fresh token required"}), 401


# ---------------------------------------------------------------------------
# Basic auth error handler - also return 401 (Flask-HTTPAuth default is 401)
# ---------------------------------------------------------------------------
@auth.error_handler
def basic_auth_error(status):
    """Handle Basic Authentication failures with a consistent 401."""
    return jsonify({"error": "Unauthorized"}), 401


if __name__ == "__main__":
    app.run(debug=False)