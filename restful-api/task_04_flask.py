#!/usr/bin/python3
"""
Develop a Simple API using Python with Flask
"""
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def return_username():
    return jsonify(list(users.keys()))


@app.route('/status')
def check_status():
    return "OK"


@app.route('/users/<username>')
def show_user_profile(username):
    return users[username]


@app.route('/add_user', methods=['POST'])
def add_user():
    my_dict = {}
    new_user = request.get_json()
    if new_user:
        username = new_user.get("username")
        if username is None:
            return jsonify({"error": "Username is required"}), 400
        my_dict["name"] = new_user.get("name")
        name = new_user.get("name")
        my_dict["age"] = new_user.get("age")
        age = new_user.get("age")
        my_dict["city"] = new_user.get("city")
        city = new_user.get("city")
        users[username] = {
            "name": name,
            "age": age,
            "city": city
        }
        return jsonify({
            "message": "Your account has been registered",
            "name": name,
            "age": age,
            "city": city
            }
            ), 201


if __name__ == "__main__":
    app.run()
