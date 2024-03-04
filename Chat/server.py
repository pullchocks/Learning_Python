import threading
import socket
import signal
import sys
import time
import re

class Server():
    def __init__(self, port):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.bind(('', port))
        self.listener.listen(1)
        print("Listening on port {0}".format(port))
        self.client_sockets = []
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)

    def run(self):
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

    def echo(self, message):
        print("Echoing: {0}".format(message))
        for client_socket in self.client_sockets:
            try:
                client_socket.sendall(message.encode())
            except socket.error:
                print("Unable to send message")

    def remove_socket(self, socket):
        self.client_sockets.remove(socket)

    def signal_handler(self, signal, frame):
        print("Tidying up")
        for client_socket in self.client_sockets:
            try:
                client_socket.close()
            except socket.error:
                pass
        self.listener.close()

class ClientListener(threading.Thread):
    def __init__(self, server, socket, address):
        super(ClientListener, self).__init__()
        self.server = server
        self.client_socket = socket
        self.client_address = address
        self.listening = True
        self.username = "No Username"

    def run(self):
        while self.listening:
            try:
                data = self.client_socket.recv(1024).decode()
                if data:
                    self.handle_msg(data)
            except socket.error:
                print("Unable to receive data")
                self.quit()
        print("Ending client thread for {0}".format(self.client_address))

    def quit(self):
        self.listening = False
        try:
            self.client_socket.close()
        except socket.error:
            pass
        self.server.remove_socket(self.client_socket)
        self.server.echo("{0} has quit. \n".format(self.username))

    def handle_msg(self, data):
        print("{0} sent: {1}".format(self.username, data))
        username_result = re.search('^USERNAME (.*)$', data)
        if username_result:
            self.username = username_result.group(1)
            self.server.echo("{0} has joined. \n".format(self.username))
        elif data == "QUIT":
            self.quit()
        elif data == "":
            self.quit()
        else:
            self.server.echo(data)

if __name__ == "__main__":
    server = Server(59091)
    server.run()
