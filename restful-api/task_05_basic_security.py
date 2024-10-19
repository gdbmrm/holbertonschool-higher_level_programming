#!/usr/bin/python3
"""
API Security and Authentication Techniques
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

secret = secrets.token_hex(32)
# clé secrete


@auth.verify_password
def check_user(username, password):
    """
    basic authentication
    """
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_authentication(username, password):
    """
    basic authentication
    """
    return "Basic Auth: Access Granted", 200


@app.route("/login", methods=["POST"])
def login():
    """
    method to log
    """
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = users.get(username)

    if not user:
        return jsonify({"error": "Invalid user"}), 401

    passwd = check_password_hash(user["password"], password)

    if passwd is False:
        return jsonify({"error": "Invalid user"}), 401

    access_token = create_access_token(identity={
        "username": username,
        "role": user["role"]})
    return jsonify(access_token=access_token), 200


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected_route():
    """
    check the jwt
    """
    return "JWT Auth: Access Granted", 200


@app.route('/admin-only')
@jwt_required()
def admins_only():
    """
    check if the user is an admin
    """
    username = request.json.get("username", None)
    user = users.get(username)

    if get_jwt_identity()["role"] not "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    handle_unauthorized_error
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    unauthorized error
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    invalid token loader
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    handle expired token error
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    handle revoked token error
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    handle needs fresh token error
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run
