import socket


s = socket.socket()
print("Socket is created !! ")

s.bind(('localhost', 9999))

s.listen(3)

print("Waiting for connections..... ")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print(f"Connected to {address} {name} \n")
    r = f'Hello {name}'
    c.send(bytes(r, 'utf-8'))

    while True:
        e = input("choice snd or rec message or exit : ")
        if e == 'snd':
            msg = input("Enter The Massage : ")
            c.send(bytes(msg, 'utf-8'))
        elif e == 'rec':
            print(c.recv(1024).decode())
        if e == 'exit' or e is None:
            break
    break

c.close()

