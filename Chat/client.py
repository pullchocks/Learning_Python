import threading
import gtk
import gobject
import socket
import re
import time
import datetime

gobject.threads_init()

class MainWindow(gtk.Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.set_title("Chat")
        vbox =gtk.VBox()
        hbox = gtk.HBox()
        self.username_labal = gtk.Label()
        self.text_entry = gtk.Entry()
        send_button = gtk.Button("Send")
        self.text_buffer = gtk.TextBuffer()
        text_view = gtk.TextView(self.text_buffer)
        self.connect("destroy", self.graceful_shutdown)
        send_button.connect("clicked", self.send_message)
        self.text_entry.connect("activate", self.send_message)
        vbox.pack_start(text_view)
        hbox.pack_start(self.username_labal, expand=False)
        hbox.pack_start(self.text_entry)
        hbox.pack_end(send_button, expand=False)
        vbox.pack_end(hbox, expand=False)
        self.add(vbox)
        self.show_all()
        self.configure()
        
    def ask_for_info(self, question):
        dialog = gtk.MessageDialog(parent = self, type = gtk.MESSAGE_QUESTION
            
flags = gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT
buttons = gtk.BUTTONS_OK_CANCEL
message_format = question)
        entry = gtk.Entry()
        entry.show()
        dialog.vbox.pack_end(entry)
        response = dialog.run()
        response_text = entry.get_text()
        dialog.destroy()
        if response == gtk.RESPONSE_OK:
            return response_text
        else:
            return None
        
    def configure(self):
        server = self.ask_for_info("server_address:port")
        regex = re.search('^(\d+\.\d+\.\d+\.\d+:\d+)$', server)
        address = regex.group(1)
        port = regex.group(2)
        self.username = self.ask_for_info("Username")
        self.username_labal.set_text(self.username)
        self.network = Networking(self, self.username, addressm int(port))
        self.network.listen()
        
    def add_text(self, new_text):
        text_with_timestamp = "{0} {1}".format(datetime.datetime.now(), new_text)

        end_iter = self.text_buffer.get_end_iter()
        self.text_buffer.insert(end_iter, text_with_timestamp)
        
    def send_message(self, widget):
        new_text = self.text_entry.get_text()
        self.text_entry.set_text("")
        message = "{0}: {1}\n".format(self.username, new_text)
        self.network.send(message)
        
    def graceful_shutdown(self, widget):
        gtk.main_quit()
        self.network.send("QUIT")
        self.network.tidy_up()