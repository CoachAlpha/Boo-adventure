import time
import socket
import os

os.system('cls')
socket_server = socket.socket()
server_host = socket.gethostname()

ip = socket.gethostbyname(server_host)

port = 8080

print('This is your IP address: ',ip)
server_host = input('Enter host\'s IP address: ')
name = input('Enter your username: ')


socket_server.connect((server_host, port))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name,' has joined...\n\n')

def send():
    message = input("\nMe : ")
    socket_server.send(message.encode())

while True:
    try:
        send()
    except:
        print("there is a Problem in the script!")
        time.sleep(5)
        exit()