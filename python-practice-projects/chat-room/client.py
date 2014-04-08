#!/usr/bin/env python

__author__ = 'Rio'

import socket
import sys

class Client(object):
    HOST_NAME = '127.0.0.1'
    PORT_NUMBER = 8000

    def __init__(self, socket=None):
        if socket is None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socket = socket

    def connect(self, hostname=None, port=0):
        if hostname is None:
            if port == 0:
                self.socket.connect((HOSTNAME, PORT))
            else:
                self.socket.connect((HOSTNAME, port))
        else:
            self.socket.connect((hosthame, port))

    def disconnect(self):
        self.socket.disconnect()
        self.socket.close()

    def send(self, msg):
        if self.socket:
            sent = self.socket.send(msg)
            if sent == 0:
                raise RuntimeError("Socket connection broken")

    def recieve(self):
        msg = ''
        chunk = self.socket.recv(1024)
        if chunk == '':
            raise RuntimeError("Socket connection broken")
        msg = chunk
        return msg
