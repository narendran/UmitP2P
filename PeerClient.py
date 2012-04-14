import socket
from Constants import *

class PeerClient:
	def __init__(self):
		self.__initialize()
		

	def __initialize(self):
		self.maxpeers = MAX_PEERS
		self.peerId = 1001 #TODO : Should think of a mechanism to make it gloally unique
		self.IPAddr = self.getIp();

	def getIp(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.connect(("google.com",80))
		return s.getsockname()[0]



peerClient = PeerClient()