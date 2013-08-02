import socket

__author__ = 'amucci'

class Dect_Sip_Rfp(object):
    socket = None

    def __init__(self, ip_omm, username, password):
        self.ip = ip_omm
        self.port = 12622
        self.username = username
        self.password = password
        self.connect()

    def send_message(self, message):
        try:
            self.socket.send(message)
        except socket.error:
            raise ValueError('Error sending message socket')

    def receive_message(self):
        return self.socket.recv(10)

    def close(self):
        self.socket.close()

    def connect(self):
        if self.socket is None:
            self.socket = socket.socket(socket.AF_INET)
            self.socket.connect((self.ip, self.port))
            print self.receive_message()

    def authorize(self):
        autorization = '<Open seq="250" username="%s" password="%s" />'%((self.username, self.password))
        print autorization
        autorization += "\0"
        self.send_message(autorization)
        print self.receive_message()
