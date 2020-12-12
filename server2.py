import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=socket.gethostname()
host=socket.gethostbyname(name)
port=8000
s.bind((host,port))
s.listen(1)
print(name)
print("waiting to be connected")
conn,addr=s.accept()
print(addr,"has been connected")
print("Type quit() to exit")
s_name=input(str("Enter your name:"))
s_name=s_name.encode()
conn.send(s_name)
r_name=conn.recv(1024)
r_name=r_name.decode()
print(r_name,"joined the room")
while True:
    rec=conn.recv(1024)
    rec=rec.decode()
    print(r_name,":",rec)
    message=input(str("Me:"))
    if message=="quit()":
        m=s_name+b" has left the room"
        conn.send(m)
        break
    message=message.encode()
    conn.send(message)
