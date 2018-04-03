import socket
import fcntl
import struct
import datetime
import time
import sys

print ("hello man")
def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

print(get_ip_address('wlan0'))  # '192.168.0.110'

now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%d-%m-%Y %H:%M:%S"))
looperCPU = 10
start = time.time()
while (looperCPU != 0):
	#this is the computation for 30 secs
       	time.sleep(30)
	print(time.time())
       	#print(now()) 
       	looperCPU -= 1    
