# Hello World program in Python
    
#python 2.7.12

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12347

try:
    s.bind(('', port))
except:
    port += 1
    s.bind(('', port))

port_number = port

print("The port number is " + str(port))
s.listen(5)
c, addr = s.accept()      

while True:
    message = input("Message: ")
    # send a thank you message to the client.  
    c.sendall(message.encode("utf-8")) 
    rec = c.recv(1024)
    print(rec)

    
    #127.0.0.1
    
    
    
    
    
    
