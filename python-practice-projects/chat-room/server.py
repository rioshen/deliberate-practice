#!/usr/bin/env python

__author__ = 'Rio'

class Server(object):
    def __init__(self, socket=None):
        if socket is None:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.socket = socket

    def run(self
