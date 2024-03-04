import socket
import threading
import time
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.server = simpledialog.askstring("Input", "Server address:port", parent=self.window)
        if self.server is None:
            self.window.destroy()
            return
        self.username = simpledialog.askstring("Input", "Username", parent=self.window)
        if self.username is None:
            self.window.destroy()
            return
        try:
            split_server = self.server.split(':')
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((split_server[0], int(split_server[1])))
        except Exception as e:
            messagebox.showerror("Connection Error", str(e))
            self.window.destroy()
            return
        self.listening = True
        self.send(f"USERNAME {self.username}")
        self.setup_ui()
        self.listen()

    def setup_ui(self):
        self.text_area = scrolledtext.ScrolledText(self.window)
        self.text_area.pack()
        self.entry = tk.Entry(self.window)
        self.entry.pack()
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message)
        self.send_button.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def listener(self):
        while self.listening:
            try:
                data = self.socket.recv(1024).decode()
                if data:
                    self.window.after(0, lambda: self.add_text(data))
            except Exception as e:
                print("Error receiving data:", e)
                break
            time.sleep(0.1)

    def listen(self):
        self.listen_thread = threading.Thread(target=self.listener)
        self.listen_thread.daemon = True
        self.listen_thread.start()

    def send_message(self):
        message = self.entry.get()
        if message:
            self.send(f"{self.username}: {message}\n")
            self.entry.delete(0, tk.END)

    def send(self, message):
        try:
            self.socket.sendall(message.encode())
        except Exception as e:
            messagebox.showerror("Send Error", str(e))

    def add_text(self, text):
        self.text_area.insert(tk.END, text + '\n')
        self.text_area.see(tk.END)

    def tidy_up(self):
        self.listening = False
        try:
            self.socket.sendall("QUIT".encode())
            self.socket.close()
        except Exception as e:
            print("Error closing socket:", e)

    def on_closing(self):
        self.tidy_up()
        self.window.destroy()

if __name__ == "__main__":
    mw = MainWindow()
    tk.mainloop()
