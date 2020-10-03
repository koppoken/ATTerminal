#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Set Reactor LED GPIO
#GPIO.setup(7,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(3,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)

print 'setup pins'

#Set Void Sheild LED GPIO
GPIO.setup(33,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(35,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(37,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(36,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(38,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(40,GPIO.OUT, initial=GPIO.LOW)

#Set Head LED GPIO
GPIO.setup(16,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23,GPIO.OUT, initial=GPIO.LOW)

#Set Head Crit LED GPIO
GPIO.setup(24,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29,GPIO.OUT, initial=GPIO.LOW)


#The Titan Traints
Reactor = 1
Voids = 1
Head = 1
Body = 1
Legs = 1
HeadCrit = 0
BodyCrit = 0
LegsCrit = 0

# Button States
PRUp = 'Open'
PRDown = 'Open'
VSUp =  'Open'
VSDown =  'Open'
HUp =  'Open'
#HDown =  'Open' moved to up only
BUp =  'Open'
#BDown =  'Open'  moved to up only
LUp =  'Open'
#LDown =  'Open'  moved to up only
HCUp =  'Open'
HCDown =  'Open'
BCUp =  'Open'
BCDown =  'Open'
LCUp =  'Open'
LCDown = 'Open'
PRUPSC = 0
PRDNSC = 0
VSUPSC = 0
VSDNSC = 0
VSBothCount = 0
HUPSC = 0
#HDNSC = 0  moved to up only
HCUPSC = 0
HCDNSC = 0

#The pins on IC2 will be my input button pins

#The pins on IC2 will be output pins

#The pins on GIPO will be output pins



# set the base number of ic1, this can be any number above (not including) 64
ic1_pin_base = 65
# pin number to code number:
# 1 = 65, 2 = 66, 3 = 67, 4 = 68, 5 = 69, 6 = 70, 7 = 71, 8 = 72, 9 = 73, 10 = 74, 11 = 75, 12 = 76, 13 = 77, 14 = 78, 15 = 79, 16 = 80
# define the i2c address of ic1, this is set by the jumpers on the HAT
ic1_i2c_addr = 0x24

# set the base number of ic2, this can be any number above (not including) 80. Pins 65 - 80 have been allocated to IC1 as defined above.
ic2_pin_base = 81
# pin number to code number:
# 1 = 81, 2 = 82, 3 = 83, 4 = 84, 5 = 85, 6 = 86, 7 = 87, 8 = 88, 9 = 89, 10 = 90, 11 = 91, 12 = 92, 13 = 93, 14 = 94, 15 = 95, 16 = 96
# define the i2c address of ic2, this is set by the jumpers on the HAT
ic2_i2c_addr = 0x20

# initiate the wiringpi library
wiringpi.wiringPiSetup()
# enable ic1 on the mcp23017 hat
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)
wiringpi.mcp23017Setup(ic2_pin_base,ic2_i2c_addr)

# setup led pins
#blue_led = 65
#yellow_led = 66
#red_led = 67
#green_led = 68

# setup switch pins
#1st rack of switches on IC1 to spread LED Load Across both IC
RUP_switch = 65
RDN_switch = 66
VSUp_switch =  67
VSDown_switch =  68
HUp_switch =  69
#HDown_switch =  70
HCUp_switch =  70
HCDown_switch =  71


#2nd rack of switches on IC2 to spread LED Load Across both IC
BUp_switch =  81
#BDown_switch =  82
BCUp_switch =  82
BCDown_switch =  83
LUp_switch =  84
#LDown_switch =  86
LCUp_switch = 85
LCDown_switch = 87


# set the pin mode to an output, 1, for all our leds
#wiringpi.pinMode(blue_led,1)
#wiringpi.pinMode(yellow_led,1)
#wiringpi.pinMode(red_led,1)
#wiringpi.pinMode(green_led,1)
# set all the leds off to start with, 0
#wiringpi.digitalWrite(blue_led,0)
#wiringpi.digitalWrite(yellow_led,0)
#wiringpi.digitalWrite(red_led,0)
#wiringpi.digitalWrite(green_led,0)

# set the pin mode to an input, 0, for all our switches
wiringpi.pinMode(RUP_switch,0)
wiringpi.pinMode(RDN_switch,0)
wiringpi.pinMode(VSUp_switch,0)
wiringpi.pinMode(VSDown_switch,0)
wiringpi.pinMode(HUp_switch,0)
#wiringpi.pinMode(HDown_switch,0)
wiringpi.pinMode(HCUp_switch,0)
wiringpi.pinMode(HCDown_switch,0)
# the mcp23017 ic has an internal pull up resistor. enabling this will keep the output pulled high. this stops any floating states which could cause odd things to happen in our script, 2
wiringpi.pullUpDnControl(RUP_switch,2)
wiringpi.pullUpDnControl(RDN_switch,2)
wiringpi.pullUpDnControl(VSUp_switch,2)
wiringpi.pullUpDnControl(VSDown_switch,2)
wiringpi.pullUpDnControl(HUp_switch,2)
#wiringpi.pullUpDnControl(HDown_switch,2)
wiringpi.pullUpDnControl(HCUp_switch,2)
wiringpi.pullUpDnControl(HCDown_switch,2)




# create an infinite loop
while True:
	# because we set the pull up resistor on our output, when we press the button the pin state will actually go low. so we need to check when the pin is low, hense the not in the if statement
	#if not wiringpi.digitalRead(blue_switch):
	#	wiringpi.digitalWrite(blue_led,1)
	#	GPIO.output(8, GPIO.HIGH)
	#else:
	#	wiringpi.digitalWrite(blue_led,0)
	#	GPIO.output(8, GPIO.LOW)
  # if not wiringpi.digitalRead(yellow_switch):
	#	wiringpi.digitalWrite(yellow_led,1)
   # else:
	#	wiringpi.digitalWrite(yellow_led,0)
   # if not wiringpi.digitalRead(red_switch):
	#	wiringpi.digitalWrite(red_led,1)
  #  else:
#		wiringpi.digitalWrite(red_led,0)
 #   if not wiringpi.digitalRead(green_switch):
#		wiringpi.digitalWrite(green_led,1)
 #   else:
#		wiringpi.digitalWrite(green_led,0)
	# when we release the button the pin state changes back to high




	
	#If a press happens I compare states and if it has gone low to high change my led state
    if not wiringpi.digitalRead(RUP_switch):
	    if PRUp =='Open':
                PRUp = 'Closed'
                PRUPSC = 1
            else:
			   PRUPSC = 0
			   
    if not wiringpi.digitalRead(RDN_switch):
            if PRDown =='Open':
                PRDown = 'Closed'
                PRDNSC = 1
            else:
			   PRDNSC = 0
			   
    if PRUPSC == 1 and PRDNSC == 0:
		if Reactor > 0 and Reactor < 7:
			Reactor = Reactor + 1
		else:
			 Reactor = 1
		#print "Reactor " + str(Reactor) + " PRUp " + str(PRUp) + " PRUPSC " + str(PRUPSC) + " PRDN " + str(PRDown) + " PRDNSC " + str(PRDNSC)
			 
    if PRUPSC == 0 and PRDNSC == 1:
		if Reactor > 1 and Reactor <= 7:
			Reactor = Reactor - 1
		else:
			 Reactor = 1
		#print "Reactor " + str(Reactor) + " PRUp " + str(PRUp) + " PRUPSC " + str(PRUPSC) + " PRDN " + str(PRDown) + " PRDNSC " + str(PRDNSC)
			 
    if PRUPSC == 1 and PRDNSC == 1:
		Reactor = 1		 
		#print "Reactor " + str(Reactor) + " PRUp " + str(PRUp) + " PRUPSC " + str(PRUPSC) + " PRDN " + str(PRDown) + " PRDNSC " + str(PRDNSC)	 
    
    
    if Reactor == 1:
          GPIO.output(15, GPIO.LOW)
          GPIO.output(13, GPIO.LOW)
          GPIO.output(3, GPIO.LOW)
          GPIO.output(8, GPIO.LOW)
          GPIO.output(10, GPIO.LOW)
	  GPIO.output(11, GPIO.LOW)
				
    if Reactor == 2:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.LOW)
          GPIO.output(3, GPIO.LOW)
          GPIO.output(8, GPIO.LOW)
          GPIO.output(10, GPIO.LOW)
	  GPIO.output(11, GPIO.LOW)
	  
    if Reactor == 3:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.HIGH)
          GPIO.output(3, GPIO.LOW)
          GPIO.output(8, GPIO.LOW)
          GPIO.output(10, GPIO.LOW)
	  GPIO.output(11, GPIO.LOW)	  

    if Reactor == 4:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.HIGH)
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(8, GPIO.LOW)
          GPIO.output(10, GPIO.LOW)
	  GPIO.output(11, GPIO.LOW)

    if Reactor == 5:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.HIGH)
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.LOW)
	  GPIO.output(11, GPIO.LOW)
	  
    if Reactor == 6:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.HIGH)
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.HIGH)
	  GPIO.output(11, GPIO.LOW)	  
	  
    if Reactor == 7:
          GPIO.output(15, GPIO.HIGH)
          GPIO.output(13, GPIO.HIGH)
          GPIO.output(3, GPIO.HIGH)
          GPIO.output(8, GPIO.HIGH)
          GPIO.output(10, GPIO.HIGH)
	  GPIO.output(11, GPIO.HIGH)	  
	  	  
    #print wiringpi.digitalRead(blue_switch)    
    if wiringpi.digitalRead(RUP_switch):
        PRUp = 'Open'
        PRUPSC = 0
    if wiringpi.digitalRead(RDN_switch):
        PRDown = 'Open'
        PRDNSC = 0
	
	#Begin Void Sheild Block
    if not wiringpi.digitalRead (VSUp_switch):
	    if VSUp =='Open':
                VSUp = 'Closed'
                VSUPSC = 1
            else:
			   VSUPSC = 0
			   
    if not wiringpi.digitalRead(VSDown_switch):
            if VSDown =='Open':
                VSDown = 'Closed'
                VSDNSC = 1
            else:
			   VSDNSC = 0

    #print "VSup " + str(VSUp) + " VSDown " + str(VSDown) 
    
    if VSUPSC == 1 and VSDNSC == 0:
		if Voids > 0 and Voids < 6:
			Voids = Voids + 1

		print "Voids " + str(Voids) 
			 
    if VSUPSC == 0 and VSDNSC == 1:
		if Voids > 1 and Voids <= 6:
			Voids = Voids - 1


		print "Voids " + str(Voids)
			 
    if VSDown == 'Closed' and VSUp == 'Closed':
            VSBothCount = VSBothCount +1
    else:
	    VSBothCount = 0
    
    if VSBothCount == 100:
		if Voids > 0 :
		  Voids = -1
		else:
		  Voids = 6
  #  print "voids: " + str(Voids) + " VSup " + str(VSUp) + " VSDown " + str(VSDown) + " VSUPSC " + str(VSUPSC) +  " VSDNSC " + str(VSDNSC)
  #  print "bothCount: " + str(VSBothCount)
    
    
    if Voids == -1:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.LOW)
 
    if Voids == 1:
       GPIO.output(33, GPIO.HIGH)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.LOW)
       
    if Voids == 2:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.HIGH)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.LOW)
  
    if Voids == 3:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.HIGH)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.LOW)
 
    if Voids == 4:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.HIGH)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.LOW)
       
    if Voids == 5:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.HIGH)
       GPIO.output(40, GPIO.LOW)
       
    if Voids == 6:
       GPIO.output(33, GPIO.LOW)
       GPIO.output(35, GPIO.LOW)
       GPIO.output(37, GPIO.LOW)
       GPIO.output(36, GPIO.LOW)
       GPIO.output(38, GPIO.LOW)
       GPIO.output(40, GPIO.HIGH) 
  
    
    if wiringpi.digitalRead(VSUp_switch):
        VSUp = 'Open'
        VSUPSC = 0
    if wiringpi.digitalRead (VSDown_switch):
        VSDown = 'Open'
        VSDNSC = 0

##Head Tracker

    if not wiringpi.digitalRead(HUp_switch):
	    if HUp =='Open':
                HUp = 'Closed'
                HUPSC = 1
		print "in Hup if"
		print str(wiringpi.digitalRead(HUp_switch))
		sleep (5)
		
            else:
			   HUPSC = 0
			#   print "IN Up Else"
			   
 #   if not wiringpi.digitalRead(HDown_switch):
 #           if HDown =='Open':
 #               HDown = 'Closed'
 #               HDNSC = 1
 #           else:
 #			   HDNSC = 0
 #			#   print "In down else"

    
    
    if HUPSC == 1: #and HDNSC == 0:
         if Head < 8: 
	      Head = Head + 1
         elif Head > 7: 
	      Head = 1
 #   if HDNSC == 1 and HUPSC == 0:
 #        if Head > 1: Head = Head -1
    
    
    if wiringpi.digitalRead(HUp_switch):
        HUp = 'Open'
        HUPSC = 0
	
    print "HSC" + str(HUPSC) + " Head " + str(Head) + " Reactor" + str(Reactor)
 #   if wiringpi.digitalRead (HDown_switch):
 #       HDown = 'Open'
 #       HDNSC = 0
    
#	GPIO.output(8, GPIO.HIGH)
#	wiringpi.digitalWrite(blue_led,0)
#	sleep(1)
#	GPIO.output(8, GPIO.HIGH`)
#	wiringpi.digitalWrite(blue_led,1)
#	sleep(1)
# add a little pause for 1/10 of a second, to allow other process on the Pi to happen, we dont want to hog all the cpu :)
sleep(0.1)
