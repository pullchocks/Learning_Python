import threading
import socketserver
import re
import signal
import sys
import time

class Server()
    def __init__(self, port)
            self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listener.bind(('' , port))
            self.listener.listen(1)
            print("Listening on port {0}".format(port0))
            self.client_sockets = []
            signal.signal(signal.SIGINT, self.signal_handler)
            signal.signal(signal.SIGTERM, self.signal_handler)
            