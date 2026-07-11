from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def servingJson():
    return jsonify(users)

@app.route("/status")
def pageStatus():
    return "OK"

@app.route("/users/<username>")
def user(username):
    if not username in users:
        return jsonify({"error": "User not found"}), 404
    return jsonify(users[username])

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = data
    return jsonify({"message": "User added successfully", "user": data}), 200

if __name__ == "__main__":
    app.run(debug=True)