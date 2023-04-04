# BROADCAST SENDER

import socket

# the broadcast address, or place to route messages to be sent to every device within a network
# read more here -> https://en.ipshu.com/ipv4/255.255.255.255
BCAST_ADDR = '255.255.255.255'
BCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# enable broadcasting mode
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(b'Hello, World!', (BCAST_ADDR, BCAST_PORT))