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
        self.end_headers()
        self.wfile.write(b'Hello, this is a simple API!')
        if "\data" in self.path:
            try:
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                my_dict = {"name": "John", "age": 30, "city": "New York"}
                dataset = json.dump(my_dict)
                self.wfile.write(dataset) 
            except:
                elf.send_response(404)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')


httpd = HTTPServer(('', 8000), My_SubClass)
httpd.serve_forever()
