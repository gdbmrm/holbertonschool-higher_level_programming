#!/usr/bin/python3

from flask import Flask, jsonify, request


users = {
      "user1": {"username": "user1", "password": "<hashed_password>", "role": "user"},
      "admin1": {"username": "admin1", "password": "<hashed_password>", "role": "admin"}
  }



@app.route('/basic-protected')
def basic_authentication():
    """
    basic authentication
    """
    return "Basic Auth: Access Granted", 200
