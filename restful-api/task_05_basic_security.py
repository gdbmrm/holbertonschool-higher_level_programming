#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
  }



@app.route('/basic-protected')
@auth.login_required
def basic_authentication():
    """
    basic authentication
    """
    return "Basic Auth: Access Granted", 200

@app.route('/login', methods=["POST"])
def jwt_auth(username, password):

@app.route('/jwt-protected')
def jwt_protected_route():
    return "JWT Auth: Access Granted"

@app.route('admin-only')
def admin_only():
    return "Admin Access: Granted"

