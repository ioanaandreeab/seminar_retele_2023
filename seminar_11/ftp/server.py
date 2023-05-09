import os

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def main():
    # instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user('user', '12345', 'server_storage', perm='elradfmwMT')
    authorizer.add_anonymous(os.getcwd())

    # instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('', 2121)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()

if __name__ == '__main__':
    main()
