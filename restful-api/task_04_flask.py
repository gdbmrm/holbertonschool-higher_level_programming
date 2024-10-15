#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    welcome message
    """
    return "Welcome to the Flask API!", 200


@app.route('/data')
def return_username():
    """
    return all the username stored
    """
    return jsonify(list(users.keys())), 200


@app.route('/status')
def check_status():
    """
    check the status return ok
    """
    return "OK", 200


@app.route('/users/<username>')
def show_user_profile(username):
    """
    return user profil if user exist
    """
    user = users.get(username)
    name = users.get("name")
    age = users.get("age")
    city = users.get("city")
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "username": username,
        "name": user["name"],
        "age": user["age"],
        "city": user["city"]
        }), 200


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    add user and return a message
    """
    my_dict = {}
    new_user = request.get_json()
    if new_user:
        username = new_user.get("username")
        if username is None:
            return jsonify({
                "error": "Username is required"}), 400

        name = new_user.get("name")
        if name is None or not isinstance(name, str):
            return jsonify({
                "error": "Name is required in string format"}), 400

        age = new_user.get("age")
        if age is None or not isinstance(age, int):
            return jsonify({
                "error": "Age is required in int format"}), 400

        city = new_user.get("city")
        if city is None or not isinstance(city, str):
            return jsonify({
                "error": "City is required in string format"}), 400

        users[username] = {
            "name": name,
            "age": age,
            "city": city
        }
        return jsonify({
            "message": "Your account has been registered",
            "user": new_user
            }), 201
    else:
        return jsonify({"error": "No data"}), 400


if __name__ == "__main__":
    app.run()
