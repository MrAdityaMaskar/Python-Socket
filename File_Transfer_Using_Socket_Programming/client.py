import socket

c = socket.socket()

c.connect(('localhost', 9999))
print("Connected to server....")
a = input("Enter Your Name: ")
c.send(bytes(a, 'utf-8'))
print(c.recv(1024).decode())
while True:

    a = input("Enter Your Choice receive (rec) or send (snd) or (file) to transfer or receive: ")
    if a == 'rec':
        print(c.recv(1024).decode())
    elif a == 'snd':
        a = input("Enter Your Message: ")
        c.send(bytes(a, 'utf-8'))

    elif a == 'file':
        k = input("Send(sndf) a file or Receive (recf) file: ")
        if k == 'sndf':
            file_name = input(str("Enter File Name: "))
            fileo = open(file_name, 'r')
            file = fileo.read(1024)
            c.send(file)
            fileo.close()
            print("Data has been successfully sent.")
            print(c.recv(1024).decode())
        if k == 'recf':
            file_name = input(str("Ente a file name for new file: "))
            file = open(file_name, 'w')
            file_data = c.recv(1024).decode()
            file.write(file_data)
            file.close()
            print("Data has been successfully received ")
            c.send(bytes(f"{file_name} is received by client ", 'utf-8'))
        else:
            pass
    elif a == 'exit':
        break

c.close()
