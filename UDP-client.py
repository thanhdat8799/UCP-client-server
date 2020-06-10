import socket
serverName = 'localhost'
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = raw_input('Input lowercase sentence:') 
clientSocket.sendto(message,(serverName, serverPort)) 
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print (modifiedMessage)
clientSocket.close()

# import socket
# import sys

# # Create a UDP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# server_address = ('localhost', 12000)
# message = raw_input('Enter your name:')



#     # Send data
# print ('sending...')
# sent = sock.sendto(message, server_address)

#     # Receive response
# print >>sys.stderr, 'waiting to receive'
# data, server = sock.recvfrom(2048)
# print >>sys.stderr, 'received "%s"' % data

# print >>sys.stderr, 'closing socket'
# sock.close()
