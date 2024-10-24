#!/usr/bin/python3
"""
Develop a simple API using Python with the `http.server` module
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class My_SubClass(BaseHTTPRequestHandler):
    """
    sub class
    """
    def do_GET(self):
        """
        method do_get that handle get request
        """
        # si l'endpoint est /data
        if self.path == "/data":
            # status code 200 ok
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            # conversion dictionnaire en json et en bytes pour affichage
            my_dict = {"name": "John", "age": 30, "city": "New York"}
            dataset = json.dumps(my_dict).encode('utf-8')
            self.wfile.write(dataset)
        elif self.path == "/status":
            # si l'endpoint est /status
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        elif self.path == "/":
            # si pas d'endpoint
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        else:
            # si erreur status code 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


httpd = HTTPServer(('', 8000), My_SubClass)
httpd.serve_forever()
