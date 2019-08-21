import socket

port = int(input("Enter the port number: "))
ip = input("Enter the IP address: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((ip, port))

while True:
    rec = s.recv(1024)
    print(rec)
    message = input("Message: ")
    s.sendall(message.encode("utf-8")) 

s.close()