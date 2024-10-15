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
    new_user = request.get_json()
    if new_user:
        username = new_user.get("username")
        if username is None:
            return "\"error": "Username is required"", 400
        key = new_user.get("key")
        users[username] = key
        return "Your account has been registered", 201


if __name__ == "__main__":
    app.run()
