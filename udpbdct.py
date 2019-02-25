import socket
import os
import sys
import time

sender = len(sys.argv) > 1 and sys.argv[1].lower() == "sender"

UDP_IP = os.getenv("UDP_IP", "0.0.0.0")
UDP_PORT = int(os.getenv("UDP_PORT", 3000))

print "Sender", sender
print "UDP IP", UDP_IP
print "UDP PORT", UDP_PORT

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if sender:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
else:
    sock.bind((UDP_IP, UDP_PORT))

stop = False
while not stop:
    try:
        if sender:
            MESSAGE = "IM HAVING THE "+ time.ctime()+ " OF MY LIFE"
            print "new MESSAGE \"", MESSAGE, "\""
            sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
            time.sleep(1)
        else:
            data, addr = sock.recvfrom(1024)
            print "received message:", data
    except KeyboardInterrupt:
        stop = True
        print "Bye"