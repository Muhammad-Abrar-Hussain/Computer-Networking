'''
Name: Muhammad Abrar Hussain
Roll No: BSCS_2020_62

'''


import socket
Host = '127.0.0.1'
Port = 50007
print("Server is running")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))
data = input("Enter data to send into server:")
if data == "":
    data = "Hello World"
s.sendall(data.encode())
data = s.recv(1024)
print("Received from server:", data.decode())
s.close()
    
    
    

