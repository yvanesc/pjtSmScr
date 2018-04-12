# display the menu
#
# connect to the db and create meanu
#
# out: print
# in : db
import os
import sys
import time

rectDis = "rect"
triDis = "triangle"
xDis = "croix"
while True:
	os.system('clear')
	#11car. for shutdown
	print"<- Shutdown"
	print"                light on->"
	print""
	print"<- " + rectDis
	print""
	print""
	print"<- " + triDis
	print""
	#print""
	#perfect length 26car.
	print"<- " + xDis + "       light off->" + "\n"
	time.sleep(10)
