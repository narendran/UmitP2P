class Peer:
	def __init__(self):
		print "Peer is on!"

	#placeholders
	def __initialize(self):
		#Initialise nodeID, maxpeers,listening port and the IP address

	def __shutdown(self):
		#Close all connections related to this peer
		#Shutdown the peer

	def addpeer(self):
		#Add a new peer to the list of peers

	def removepeer(self):
		#remove the particular peer from the peer list

	def sendmsg(self,peerid):
		#Create a new connection object which will handle the send/receive mechanism for this msg.
		#Pass the connection object and the msg to handler
		#This should be flexible to allow any specific send/receive mechanism to be plugged in. Eg: UMIT has its own send/receive mechanism

	def delegator(self):
		#decides which handler should take care of the new peer msg.

	def serverloop(self):
		#this method will be continuously listening for incoming connections in the port specified.

peer = Peer();