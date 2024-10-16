#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)

users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
  }

secret = secrets.token_hex(32)
# clé secrete


@app.route('/basic-protected')
@auth.login_required
def basic_authentication(username, password):
    """
    basic authentication
    """
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token), 200

@app.route('/jwt-protected')
def jwt_protected_route():
    return "JWT Auth: Access Granted"

@app.route('admin-only')
def admin_only():
    return "Admin Access: Granted"

if __name__ == '__main__':
    app.run