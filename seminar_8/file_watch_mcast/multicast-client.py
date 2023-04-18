import socket
import struct

MCAST_GROUP = '224.0.0.1'
MCAST_PORT = 5001
DEST_FOLDER = 'temp-receive'

FILE_SERVER = '127.0.0.1'
FILE_PORT = 12345

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((MCAST_GROUP, MCAST_PORT))

    group = socket.inet_aton(MCAST_GROUP)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        data, address = sock.recvfrom(1024)
        filename = data.decode()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((FILE_SERVER, FILE_PORT))
            s.sendall(filename.encode('utf-8'))
            data = s.recv(1024)
            print(data)
            with open(DEST_FOLDER + '/' + filename, 'wb') as f:
                f.write(data)

if __name__ == '__main__':
    main()
