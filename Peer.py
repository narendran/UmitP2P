import sys
import socket
from Constants import *

class PeerClient:
	def __init__(self):
		self.__initialize()
		

	def __initialize(self):
		self.maxpeers = MAX_PEERS
		self.peerId = 1001 #TODO : Should think of a mechanism to make it gloally unique
		self.IPAddr = self.getIp()
		self.listenport = int(sys.argv[1])
		self.print_peerdetails()
		self.listenLoop()

	def getIp(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		s.connect(("google.com",80))
		return s.getsockname()[0]

	def print_peerdetails(self):
		print "Max Peers : ",self.maxpeers
		print "Peer ID : ",self.peerId
		print "IP Address : ",self.IPAddr
		print "Listening for connections on : ",self.listenport

	def createserversock(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((self.IPAddr,self.listenport))
		s.listen(BACKLOG)
		return s;

	def listenLoop(self):
		sock = self.createserversock();
		while(1):
			try:
				clientsock, clientaddr = sock.accept()
				print "New PeerConnection at - ",clientaddr," with client socket :",clientsock
				data = clientsock.recv(BUFFER_SIZE)
				print "From PeerClient : ",data

			except KeyboardInterrupt:
				print "Killing the Listen Loop due to  KeyBoard Interrupt"
				break

		sock.close();

	def __shutdown(self):
		#Close all connections related to this peer
		#Shutdown the peer
		print

	def addpeer(self):
		#Add a new peer to the list of peers
		print

	def removepeer(self):
		#remove the particular peer from the peer list
		print

	def sendmsg(self,peerid):
		#Create a new connection object which will handle the send/receive mechanism for this msg.
		#Pass the connection object and the msg to handler
		#This should be flexible to allow any specific send/receive mechanism to be plugged in. Eg: UMIT has its own send/receive mechanism
		print

	def delegator(self):
		#decides which handler should take care of the new peer msg.
		print


peerClient = PeerClient()