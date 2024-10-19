#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    welcome message
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def return_username():
    """
    return all the username stored
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def check_status():
    """
    check the status return ok
    """
    return "OK"


@app.route("/users/<username>")
def show_user_profile(username):
    """
    return user profil if user exist
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add user and return a message
    """
    new_user = request.get_json()
    if not new_user or "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400

    username = new_user["username"]

    users[username] = {
        "username": username,
        "name": new_user.get('name', ''),
        "age": new_user.get('age', 0),
        "city": new_user.get('city', '')
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
        }), 201


if __name__ == "__main__":
    app.run(debug=True)
