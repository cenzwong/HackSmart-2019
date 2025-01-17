#!/usr/bin/env python3

import serial
from time import sleep
ser = serial.Serial('COM12', 9600)  ## 9600是你的baud rate
ser.flush()


from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys
PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    print(data)

    ser.write(data)

sys.exit()