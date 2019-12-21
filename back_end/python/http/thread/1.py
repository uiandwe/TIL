# -*- coding: utf-8 -*-
import http.server
import socket
import _thread

class StoppableHTTPServer(http.server.HTTPServer):

    def server_bind(self):
        http.server.HTTPServer.server_bind(self)
        self.socket.settimeout(1)
        self.run = True

    def get_request(self):
        while self.run:
            try:
                sock, addr = self.socket.accept()
                sock.settimeout(None)
                return (sock, addr)
            except socket.timeout:
                pass

    def stop(self):
        self.run = False

    def serve(self):
        while self.run:
            self.handle_request()

if __name__=="__main__":
    httpd = StoppableHTTPServer(("127.0.0.1",8080), http.server.SimpleHTTPRequestHandler)
    _thread.start_new_thread(httpd.serve, ())
    input("Press <RETURN> to stop server\n")
    httpd.stop()
