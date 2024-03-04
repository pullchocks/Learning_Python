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
            
    def run(self))
        while True:
            print("Listening for more clients")
            
            try:
                client_socket, client_address = self.listener.accept()
            except socket.error:
                sys.exit("Could not accept any more connections")
                
            self.client_sockets.append(client_socket)
            
            print("Starting client thread for {0}".format(client_address))
            client_thread = ClientListener(self, client_socket, client_address)
            client_thread.start()
            
            time.sleep(0.1)
            
    def echo(self, message)
        print("Echoing: {0}".format(data))
        
        try:
            socket.sendall(data)
        except socket.error:
            print("Unable to send message")
            
    def remove_socket(self, socket)
        self.client_sockets.remove(socket)
    def signal_handler(self, signal, frame)
        print("Tidying up")
        self.listener.close()
        self.echo("QUIT")
        
client_thread.start()
