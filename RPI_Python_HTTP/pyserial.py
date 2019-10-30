import serial
from time import sleep
ser = serial.Serial('COM12', 9600)  ## 9600是你的baud rate
ser.flush()
ser.write(b'a')
ser.write(b'b')