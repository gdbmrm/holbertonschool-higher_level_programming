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

    name = users.get("name")
    age = users.get("age")
    city = users.get("city")
    return jsonify({
        "username": username,
        "name": user["name"],
        "age": user["age"],
        "city": user["city"]
        }), 200


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    add user and return a message
    """
    my_dict = {}
    new_user = request.get_json()
    if new_user.get("username") not in users:
        return jsonify({"error": "User already registered"}), 409

    if new_user is not None:
        return jsonify({"error": "No data"}), 400

    if not request.json.get("username"):
        return jsonify({"error": "Username is required"}), 400
    username = new_user.get("username")

    if not request.json.get("name") or not isinstance(name, str):
        return jsonify({
            "error": "Name is required in string format"}), 400
    name = new_user.get("name")

    if not request.json.get("age") or not isinstance(age, int):
        return jsonify({
            "error": "Age is required in int format"}), 400
    age = new_user.get("age")

    if not request.json.get("city") or not isinstance(city, str):
        return jsonify({
            "error": "City is required in string format"}), 400
    city = new_user.get("city")

    users[username] = {
        "name": name,
        "age": age,
        "city": city
    }
    return jsonify({
        "message": "User added",
        "user": new_user
        }), 201



if __name__ == "__main__":
    app.run()
