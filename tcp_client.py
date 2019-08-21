import socket

port = int(input("Enter the port number: "))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

print(s.recv(1024))

s.close()