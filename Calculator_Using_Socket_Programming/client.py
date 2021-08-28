import socket

c = socket.socket()

c.connect(('localhost', 9999))
print("Connected to server....")
a = input("Enter Your Name: ")

c.send(bytes(a, 'utf-8'))
print(c.recv(1024).decode())
while True:
    a = input("Enter Your Choice, Solve or exit : ")
    if a == 'Solve':
        ab = map(str, input("Enter Expression as example(2 + 3) : ").split(' '))
        abc = list(ab)
        y = str(abc)
        c.send(y.encode())
        i = c.recv(1024).decode()
        print(f'Your answer for {abc[0]}{abc[1]}{abc[2]} is ', float(i))
    if a == 'exit':
        break

c.close()
