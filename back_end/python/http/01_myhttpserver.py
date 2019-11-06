# -*- coding: utf-8 -*-
from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("pass get")
        self.wfile.write("hello world".encode())

if __name__ == '__main__':
    server = HTTPServer(('', 8888), MyHandler)
    print("server start")
    server.serve_forever()
