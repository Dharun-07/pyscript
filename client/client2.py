import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
name=input(str("Enter the device name you want to be connected:"))
port=8000
s.connect((name,port))
print(name,"has been connected")
print("Type quit() to exit")
s_name=input(str("Enter your name:"))
s_name=s_name.encode()
s.send(s_name)
r_name=s.recv(1024)
r_name=r_name.decode()
print(r_name,"joined the room")
while True:
    message=input(str("Me:"))
    message=message.encode()
    if message=="quit()":
        m=s_name+b" has left the room"
        s.send(m)
        break
    s.send(message)
    rec=s.recv(1024)
    rec=rec.decode()
    print(r_name,":",rec)
