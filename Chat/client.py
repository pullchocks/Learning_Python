import socket
import threading
import time
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class MainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat Client")
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
        
        self.setup_ui()
        self.listening = True
        self.listen()

        self.send(f"USERNAME {self.username}")

    def setup_ui(self):
        self.text_area = tk.Text(self.window, wrap=tk.WORD, state='disabled')
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        self.scrollbar = ttk.Scrollbar(self.window, orient="vertical", command=self.text_area.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.text_area['yscrollcommand'] = self.scrollbar.set
        
        self.entry_frame = ttk.Frame(self.window)
        self.entry_frame.pack(expand=True, fill=tk.BOTH, padx=10)

        self.entry = ttk.Entry(self.entry_frame)
        self.entry.pack(side="left", expand=True, fill=tk.BOTH, pady=5)
        self.entry.focus_set()

        self.send_button = ttk.Button(self.entry_frame, text="Send", command=self.send_message)
        self.send_button.pack(side="right", padx=5, pady=5)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

    def listener(self):
        while self.listening:
            try:
                data = self.socket.recv(1024).decode()
                if data:
                    self.window.after(0, lambda d=data: self.add_text(d))
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
            formatted_message = f"{self.username}: {message}"
            self.add_text(formatted_message)
            self.send(formatted_message)
            self.entry.delete(0, tk.END)

    def send(self, message):
        try:
            self.socket.sendall(message.encode())
        except Exception as e:
            messagebox.showerror("Send Error", str(e))

    def add_text(self, text):
        self.text_area.config(state='normal')
        self.text_area.insert(tk.END, f"{text}\n")
        self.text_area.config(state='disabled')
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
