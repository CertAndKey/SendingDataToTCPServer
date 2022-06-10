import socket
import sys
import time

# Create TCP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind Socket to Port
server_address = ("<ip>", <port>)
print('starting up on %s:%s' % server_address)
time.sleep(2)
sock.connect(server_address)

# Connect to Socket and Send Data
print('sending data')
sock.send(bytes.fromhex('HE XD AT AT OS EN D!'))
data = sock.recv(100)
print(data)
time.sleep(3)


# Close Socket
sock.close()
