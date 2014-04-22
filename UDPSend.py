import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "$,R,10,100,G,500,1000,B,90,270,V,0,0,W,0,0,X,0,55,Y,0,0,Z,10,0,S,19,29,122\r"

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
while True:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    time.sleep(1)
