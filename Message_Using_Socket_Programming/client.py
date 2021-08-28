import socket

c = socket.socket()

c.connect(('localhost', 9999))
print("You are connected to server!! ")
name = input("Enter Your name : ")
c.send(bytes(name, 'utf-8'))
print(c.recv(1024).decode())
while True:

    e = input("choice snd or rec or exit: ")
    if e == 'snd':
        msg = input("Enter The Massage : ")

        c.send(bytes(msg, 'utf-8'))
    elif e == 'rec':
        print(c.recv(1024).decode())
    elif e == 'exit' or e is None:
        break
c.close()
