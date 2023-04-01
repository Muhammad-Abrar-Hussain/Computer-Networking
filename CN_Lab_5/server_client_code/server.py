'''
Name: Muhammad Abrar Hussain
Roll No: BSCS_2020_62

'''
import socket
Host = '127.0.0.1'
Port = 50007
Back_LOG = 5
print("server is running")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen(Back_LOG)
conn, addr = s.accept()
print('connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print("received from client:", data.decode())
    conn.sendall(data)
conn.close()
print("server is closed")
    