import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=8080
s.bind((host,port))
s.listen(1)
print(host)
print("waiting for connected---")
conn,acc=s.accept()
print(acc,"has been accepted.")
print(conn)
name=input(str("Enter the file name to send:"))
file=open(name,"rb")
file_data=file.read(10)
s.send(file_data)




