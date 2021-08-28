import socket

s = socket.socket()

s.bind(('localhost', 9999))
print("Waiting for connection....")
s.listen()
if s.listen() is True:
    print("Client is Online!!")
while True:
    c, address = s.accept()
    name = c.recv(1024).decode()
    print(f"Connected to {address} {name} \n")
    c.send(bytes(f"Hello {name}", 'utf-8'))
    while True:
        a = input("Enter Your Choice receive (rec) or send (snd) or (file) to send or recive data: ")
        if a == 'rec':
            print(c.recv(1024).decode())
        elif a == 'snd':
            a = input("Enter Your Message: ")
            c.send(bytes(a, 'utf-8'))
        elif a == 'file':
            k = input("Send (sndf) a file or Receive (recf) file: ")
            if k == 'sndf':
                file_name = input("Enter File Name: ")
                c.send(bytes(file_name, 'utf-8'))
                fileo = open(file_name, 'rb')
                file = fileo.read(1024)
                c.send(file)
                fileo.close()
                print("Data has been successfully sent.")
                print(c.recv(1024).decode())
            if k == 'recf':
                file_name = c.recv(1024).decode()
                file = open(file_name, 'wb')
                file_data = c.recv(1024).decode()
                file.write(file_data)
                file.close()
                print("Data has been successfully received ")
                c.send(bytes(f"{file_name} is received by client ", 'utf-8'))
            else:
                pass

        elif a == 'exit':
            break

    break
s.close()
