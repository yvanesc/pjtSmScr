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
#import asciiNbr
#import asciiTxt

# backslash remove space before & after multiline

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

loopDisplay = 5
start = time.time()
while (loopDisplay != 0):
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
        print ("|         "+ nowTime.strftime("%H:%M")+"        |")
        print("------------------------")
        print(str(dayOfWeek)+ " " + nowDay.strftime("%d")+ " "+nbMonth+"  "+nowYear)# nowMonth.strftime("%m"))
        #print(nbMonth)
        print("IP :" + get_ip_address('wlan0'))  # '192.168.0.110'
        print("Vers. Python : " + sys.version[:5])
        #print ("Current date and time : ")
        #ok it work
        #print (now.strftime("%H:%M")
        #print (now.strftime("%H:%M %d-%m-%Y"))# %H:%M:%S"))
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
        time.sleep(60)
        #refresh display every minutes
        #loopDisplay -= 1

