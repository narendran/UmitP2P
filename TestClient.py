import socket
from Constants import *
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('14.96.52.41',LISTEN_PORT))
data = raw_input(" >> ")
s.send(data)
s.close()