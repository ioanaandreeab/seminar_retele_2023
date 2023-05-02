import socket

HOST = "127.0.0.1"
PORT = 3334

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_command = ''
    while client_command.strip() != 'exit':
        client_command = input('>')
        client_socket.sendall(client_command.encode('utf-8'))
        data_received = client_socket.recv(1024)
        if not data_received:
            break
        string_data_received = data_received.decode('utf-8')
        print(string_data_received)