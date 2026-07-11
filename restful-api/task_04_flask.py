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

@app.route("/add_user/<string:x>")
def add_user(x):
    if not x:
        return jsonify({"error": "Username is required"}), 400
    try:
        z = jsonify(x)
    except Exception:
        return jsonify({"error":"Invalid JSON"}), 400
    if x.keys() in users.keys():
        return jsonify({"error":"Username already exists"}), 409
    users["usernames"] = x
    return x, 200

if __name__ == "__main__":
    app.run()