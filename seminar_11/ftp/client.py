from ftplib import FTP
import os

def main():
    # connect to the FTP server
    ftp = FTP()
    ftp.connect('localhost', 2121)
    ftp.login(user="user", passwd="12345")

    # list the files in the directory
    ftp.retrlines("LIST")

    # upload a file
    with open("user_storage\\user_file.txt", "rb") as f:
        f.seek(0)
        ftp.storbinary("STOR user_file.txt", f)

    # download a file
    with open("user_storage\\server_file.txt", "wb") as f:
        f.seek(0)
        ftp.retrbinary("RETR server_file.txt", f.write)

    # disconnect from the server
    ftp.quit()

if __name__ == '__main__':
  main()

