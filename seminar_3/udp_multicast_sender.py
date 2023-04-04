# MULTICAST SENDER

import socket

# local multicast address
# read more here -> https://en.ipshu.com/ipv4/224.1.1.1
MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5007

# AF_INET - IPv4, SOCK_DGRAM - UDP, 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# option that applies to the IP layer, setting multicast time to live to 32 hops
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)
sock.sendto(b'Hello, World!', (MCAST_GRP, MCAST_PORT))