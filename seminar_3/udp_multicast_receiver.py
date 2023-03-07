# MULTICAST RECEIVER

import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# allows multiple sockets to be bound to this same (addr, port) combination at once, i.e. you can run multiple copies of your program at once, or in quick succession
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# socket is bound to a port, listen ONLY to MCAST_GRP
sock.bind((MCAST_GRP, MCAST_PORT))
# 8-byte packed representation of the multicast group address followed by the network interface on which the server should listen for the traffic, identified by its IP address
# in this case, the receiver listens on all interfaces using INADDR_ANY
# inet_aton() converts an IPv4 address from the dotted-quad string format to 32-bit packed binary format
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
# socket is added to the multicast group by using setsockopt() to change the IP_ADD_MEMBERSHIP option
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print(sock.recv(10240))