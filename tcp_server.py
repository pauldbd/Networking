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

while True:
    c, addr = s.accept()      
    print ('Got connection from', addr )
    
    message = "Hello world"
    # send a thank you message to the client.  
    c.sendall(message.encode("utf-8")) 
    
    # Close the connection with the client 
    c.close() 
    
    
    #127.0.0.1
    
    
    