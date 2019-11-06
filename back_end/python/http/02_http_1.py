# -*- coding: utf-8 -*-
import logging
from http.server import HTTPServer, BaseHTTPRequestHandler

class FakeCollectdIngest(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/ascii")
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write("OK".encode())

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-Type", "text/ascii")
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write("OK".encode())

print('Starting ingest server on port 80')
httpd = HTTPServer(('', 8080), FakeCollectdIngest)
httpd.serve_forever()
print('Ingest server shutting down')
