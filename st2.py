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


def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def convSize(sizeHd):
	#sizeHd =int(sizeHd)
	suffixSize=['B','KB','MB','GB','TB']
	suffixI = 0
	while sizeHd > 1024 and suffixI < 4:
		suffixI += 1
		sizeHd = sizeHd/1024
	return str(sizeHd) + suffixSize[suffixI]


loopDisplay = 5
start = time.time()
imgNb=0
while (loopDisplay != 0):
	os.system("./picShoot.sh")
        imgNb+=1
	cls()
        try:
                f = urllib2.urlopen('http://api.wunderground.com/api/a71894d18588a38f/geolookup/conditions/q/ch/lausanne.json')
        except:
                f = 1
        #print ("hello man")
        #txtTest ="hello man" 
        #lenTxt = len(txtTest)	
        #print (asciiTxt.convTxt("a"))
        #for iTxt in range(lenTxt+1):
                #print (txtTest[iTxt-1:iTxt]) 
                #(asciiTxt.convTxt(txtTest[iTxt-1:iTxt])) 
        def get_ip_address(ifname):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
                )[20:24])
        nowTime = datetime.datetime.now()
        nowDay = datetime.datetime.now()
        nowMonth = datetime.datetime.now()
        nowYear = datetime.datetime.now()
        nowYear = nowYear.strftime("%Y")
        nbMonth=nowMonth.strftime("%m")
	nowFuTime = datetime.datetime.now()
	#camera.capture("image.jpg")#nowFuTime.strftime("%H%M%S"+".jpg")
        if nbMonth == "04":
                nbMonth="Avril"
        else:
                nbMonth="Nothing"
        dayOfWeek = datetime.datetime.today().weekday()
        if dayOfWeek == 0:
                dayOfWeek = "Lundi"
        elif dayOfWeek == 1:
                dayOfWeek = "Mardi"
        print("------------------------")
	#color style/color font/background color
        print ("\x1b[6;30;42m"+"|         "+ nowTime.strftime("%H:%M")+"        |"+"\x1b[0m")
        print("------------------------")
        print(str(dayOfWeek)+ " " + nowDay.strftime("%d")+ " "+nbMonth+"  "+nowYear)# nowMonth.strftime("%m"))
        #print(nbMonth)
        print("IP : " + get_ip_address('wlan0'))  # '192.168.0.110'
        print("Vers. Python : " + sys.version[:5])
	print ("OS : " + sys.platform),
	print(" / Nb img " + str(imgNb))
	statvfs=os.statvfs('/')
	print("Disk size/free : " + convSize(statvfs.f_frsize * statvfs.f_blocks) +" / "+ convSize(statvfs.f_frsize * statvfs.f_bfree))
	#print("free space : "+convSize(statvfs.f_frsize * statvfs.f_bfree))
	#print(statvfs.f_frsize * statvfs.f_bavail)

	#print(convSize(statvfs.f_frsize * statvfs.f_bavail))
	#lSize=os.stat(
	#print (lSize + bSize + sizeOnDisk)
        if f == 1:
                print("No weather informations")
        else:
                json_string = f.read()
                parsed_json = json.loads(json_string)
                location = parsed_json['location']['city']
                temp_f = parsed_json['current_observation']['temp_c']
                print "%s : %s" % (location, temp_f),
                print "C"
                f.close()
	#run script to take pic
	#os.system("./picShoot.sh")
        time.sleep(60)
        #refresh display every minutes
        #loopDisplay -= 1

