# -*- coding: utf-8 -*-

import select
import socket
import sys

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        connection_list = [s]
        while s:
            read_socket, write_socket, error_socket = select.select(connection_list, [], [], 10)

            for sock in read_socket:
                if sock == s:
                    conn, addr = s.accept()
                    print('connected by', addr)
                    connection_list.append(conn)
                else:
                    data = sock.recv(1024)
                    if not data:
                        connection_list.remove(sock)
                        sock.close()
                        break
                    sock.sendall(data)

except KeyboardInterrupt:
    sys.exit()
