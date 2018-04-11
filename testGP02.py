#!/usr/bin/python
# -*- coding: utf-8 -*- 
import RPi.GPIO as GPIO
import time
import os

print (GPIO.VERSION)

GPIO.setmode(GPIO.BCM)

#GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN)
prev_input = 0

print("here we go! Press ctrl + c to exit !")
while True:
	input = GPIO.input(23)
	if ((not prev_input) and input):
		print("pressed")
	prev_input = input
	time.sleep(0.05)
	#if (GPIO.input(23) == 0):
		#print("pressed")
