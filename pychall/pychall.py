#!/usr/bin/python
import os
import SocketServer
import sys
import pickle

class ProblemHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        
        self.wfile.write("data process service\n")

        self.wfile.write("data : ")
        data = self.rfile.read(1024)
        self.wfile.write(data)
        pick = pickle.loads(data)

        self.wfile.write("success")

class ReusableTCPServer(SocketServer.ForkingMixIn, SocketServer.TCPServer):
    allow_reuse_address = True

if __name__ == '__main__':
    HOST = '0.0.0.0'
    PORT = 8899
    SocketServer.TCPServer.allow_reuse_address = True
    server = ReusableTCPServer((HOST, PORT), ProblemHandler)
    server.serve_forever()

