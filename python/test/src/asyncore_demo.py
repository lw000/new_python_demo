#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2017年12月18日

@author: Administrator
'''

import sys
import time
import asyncore
import socket
import threading
import getopt

class EchoHandler(asyncore.dispatcher_with_send):

    def handle_read(self):
        try:
            data = self.recv(1024).decode()
            if len(data) == 0:
                pass
            
            if data:
                self.send(data.encode())
        except:
            print("error.")

class EchoServer(asyncore.dispatcher):

    def __init__(self, host, port):
#         asyncore.dispatcher.__init__(self)
        super(EchoServer, self).__init__()
        
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)

    def handle_accept(self):
        conn, addr = self.accept()
        print('Incoming connection from %s' % repr(addr))
        self.handler = EchoHandler(conn)

class EchoClient(asyncore.dispatcher):

    def __init__(self, host, port):
#         asyncore.dispatcher.__init__(self)
        super(EchoClient, self).__init__()
        
        self.messages = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))

    def handle_connect(self):
        print('handle_connect')

    def handle_close(self):
        print('handle_close')
        self.close()

    def handle_read(self):
        try:
            data = self.recv(1024)
            print(data.decode())
        except:
            print("error.")

#     def writable(self):
#         return (len(self.messages) > 0)
# 
#     def handle_write(self):
#         if len(self.messages) > 0:
#             self.send(self.messages.pop(0).encode())

class EchoServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        EchoServer('localhost', 9999)
        asyncore.loop()

class EchoClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        EchoClient('localhost', 9999)
        asyncore.loop()

if __name__ == '__main__':
    opts, _ = getopt.getopt(sys.argv[1:], '-p:-c:', ['--platform=','--config='])
    
    name = opts[0][0]
    value = opts[0][1]
    
    if value == 's':
        server = EchoServerThread()
        server.start()
        server.join()
    else:
        client = EchoClientThread()
        client.start()
        client.join()
            
#     for name, value in opts:
#         print('%s %s' % (name, value))
#         if value == 's':
#             server = EchoServerThread().start()
#             server.join()
#         else:
#             client = EchoClientThread().start()
#             client.join()
    
