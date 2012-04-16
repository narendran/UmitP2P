import socket
import sys
from Constants import *

def searchPeers():
	print "Searching peers"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# TODO : Using Command Line parameters for testing purpose.
s.connect(("14.96.88.106",int(sys.argv[1])))
data = raw_input(" >> ")
s.send(data)
s.close()