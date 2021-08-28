import socket

s = socket.socket()
s.bind(('localhost', 9999))
print('Waiting for Connection....')
s.listen()
if s.listen() is True:
    print("Client is Online!!")

while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print(f"Connected to {address} {name} \n")
    r = f'Hello {name}'
    c.send(bytes(r, 'utf-8'))

    while True:
        a = input("Enter Your Choice, receive or exit : ")
        if a == 'receive':
            a = c.recv(1024).decode()
            y = eval(a)
            if y[1] == '+':
                def x(k, m):
                    return k + m
            elif y[1] == '-':
                def x(k, m):
                    return k - m
            elif y[1] == '*':
                def x(k, m):
                    return k * m
            elif y[1] == '/':
                def x(k, m):
                    return k / m
            elif y[1] == '%':
                def x(k, m):
                    return k % m
            else:
                break
            p = x(float(y[0]), float(y[2]))

            c.send(str(p).encode('utf-8'))
            print(f"The answer for {y[0]}{y[1]}{y[2]} is {p} and sent to {name} ")
        elif a == 'exit':
            break
    break
    
c.close()
