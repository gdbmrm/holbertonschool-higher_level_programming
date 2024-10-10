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
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')


httpd = HTTPServer(('', 8000), My_SubClass)
httpd.serve_forever()
