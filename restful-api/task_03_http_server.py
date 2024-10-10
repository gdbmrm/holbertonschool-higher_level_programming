#!/usr/bin/python3
import http.server

class My_SubClass(http.server.BaseHTTPRequestHandler):
    """
    sub class
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, this is a simple API!</h1></body></html>")