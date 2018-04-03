#start deku
#start prog
import socket
import fcntl
import struct
import datetime
import time
import sys
import os
import urllib2
import json
import asciiNbr

# backslash remove space before & after multiline
n1 =""" ____  
|    | 
 |   | 
 |   | 
 |   | 
 |   | 
 |___| 
"""
n0 =""" _______ 
|  _    |
| | |   |
| | |   |
| |_|   |
|       |
|_______|
"""

nsep=""" ___  
|   | 
|___| 
 ___  
|   | 
|___| 

"""
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

loopDisplay = 5
start = time.time()
while (loopDisplay != 0):
        cls()
        f = urllib2.urlopen('http://api.wunderground.com/api/a71894d18588a38f/geolookup/conditions/q/ch/lausanne.json')
        print ("hello man")
        def get_ip_address(ifname):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
                )[20:24])

        print(get_ip_address('wlan0'))  # '192.168.0.110'
	print("Version Python : " + sys.version)
        now = datetime.datetime.now()
        print ("Current date and time : ")
        #ok it work
        #h0=now.strftime("%H")[:1]
        #h1=now.strftime("%H")[1:]
        #print(h0)
        #print(h1)
        #print(n1)
        #print(n0.join(n1)) NO
        #print(n0+n1)
        #print ((n0.split('\n',1)[0]) + (n1.split('\n',1)[0]))
        #print ((n0.split('\n',2)[0]) + (n1.split('\n',2)[0]))
	#for line in n0.split('\n'):
		#print line
	for num in range (0, 7):
		#print(len(n0.splitlines()[num]))
		h1Merge = n0.splitlines()[num]
		if len(h1Merge) < 9:
			len2Ad = 9 - len(h1Merge)
		else:
			len2Ad = 0
		h1Merge = h1Merge + " " * len2Ad
		
		h2Merge = n1.splitlines()[num]
		if len(h2Merge) < 9:  
                        len2Ad = 9 - len(h2Merge)
                else:
                        len2Ad = 0
                h2Merge = h2Merge + " " * len2Ad
		
		sepMerge = nsep.splitlines()[num]
		if len(sepMerge) < 6:
                        len2Ad = 6 - len(sepMerge)
                else:
                        len2Ad = 0
                sepMerge = sepMerge + " " * len2Ad

		m1Merge = asciiNbr.n3.splitlines()[num]
		if len(m1Merge) < 9:
                        len2Ad = 9 - len(m1Merge)
                else:
                        len2Ad = 0
                m1Merge = m1Merge + " " * len2Ad
	
		m2Merge = n1.splitlines()[num]
		if len(m2Merge) < 9:
                        len2Ad = 9 - len(m2Merge)
                else:
                        len2Ad = 0
                m2Merge = m2Merge + " " * len2Ad
		
		#use =end for Py 3
		print h1Merge, h2Merge, sepMerge, m1Merge, m2Merge
		#print (", ".join(n0.splitlines()[num], n1.splitlines()[num]))
		#print(", ".join(n0.splitlines()[num]))
	print (now.strftime("%d-%m-%Y %H:%M:%S"))
        json_string = f.read()
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_c']
        print "Current temperature in %s is: %s" % (location, temp_f)
        f.close()
        time.sleep(10)
        loopDisplay -= 1
