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
import datetime

# backslash remove space before & after multiline

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def retLin(linM, spM):
    if len(linM) < spM:
        len2Ad = spM - len(linM)
    else:
        len2Ad = 0
    linM = linM + " " * len2Ad
    return linM
def convNbr(nbr):
	if nbr == "1":
		return asciiNbr.n1	
	elif nbr == "2":
		return asciiNbr.n2
	elif nbr == "3":
		return asciiNbr.n3
	elif nbr == "4":
		return asciiNbr.n4
	elif nbr == "5":
		return asciiNbr.n5
	elif nbr == "6":
		return asciiNbr.n6
	elif nbr == "7":
		return asciiNbr.n7
	elif nbr == "8":
		return asciiNbr.n8
	elif nbr == "9":
		return asciiNbr.n9
	elif nbr == "0":
		return asciiNbr.n0

def convDay(nbDay):
	if nbDay == 0:
		return "Monday"
	elif nbDay == 1:
		return "Tuesday"
	elif nbDay == 2:
		return "Wednesday"
	elif nbDay == 3:
		return "Tuersday"
	elif nbDay == 4:
		return "Friday"
	elif nbDay == 5:
		return "Saturday"
	elif nbDay == 6:
		return "Sunday" 
	else:
		print "nonnn"
	
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
	#day of the week
	dayConv=now.weekday()
	print("Day : " +convDay(dayConv))
	print ("Current date and time : ")
        #ok it work
        h0=now.strftime("%H")[:1]
	h0=convNbr(h0)
        h1=now.strftime("%H")[1:]
        h1=convNbr(h1)
	m1=now.strftime("%M")[:1]
	m1=convNbr(m1)
	m2=now.strftime("%M")[1:]
	m2=convNbr(m2)
	for num in range (0, 7):
                #print(len(n0.splitlines()[num]))
                h1Merge = h0.splitlines()[num]
                retLin(h1Merge, 9)                

                h2Merge = h1.splitlines()[num]
                retLin(h2Merge, 9)

                sepMerge = asciiNbr.nsep.splitlines()[num]
                retLin(sepMerge, 6)

                m1Merge = m1.splitlines()[num]
                retLin(m1Merge, 9)

                m2Merge = m2.splitlines()[num]
                retLin(m2Merge, 9)

                #use =end for Py 3
                print h1Merge, h2Merge, sepMerge, m1Merge, m2Merge
        
	print (now.strftime("%d-%m-%Y %H:%M:%S"))
        json_string = f.read()
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_c']
        print "Current temperature in %s is: %s" % (location, temp_f)
        f.close()
	#refresh every minutes
        time.sleep(60)
	#loop infiny
        #loopDisplay -= 1
