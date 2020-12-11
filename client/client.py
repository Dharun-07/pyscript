import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input(str("Enter the hostname:"))
port=8080
s.connect((host,port))
print("connected>>>>")
a=s.recv(1024)
print(a.decode('ascii'))
filename=input(str("Enter the file name:"))
file=open(filename,"ab")
file_data=s.recv(1024)
file.write(file_data)
file.close()
print("file recieved sucessfully")
