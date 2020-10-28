#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

print "Off we Go"

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
print 'Done trait setup'
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
print 'wiring Pi init'
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
print 'set up switch pins'
# setup switch pins
#1st rack of switches on IC1 to spread LED Load Across both IC
RUP_switch = 73
RDN_switch = 74
VSUP_switch = 75
VSDN_switch = 76
HUP_switch = 77
BUP_switch = 78


#2nd rack of switches on IC2 to spread LED Load Across both IC
LUP_switch = 89
HCUP_switch = 90
HCDN_switch = 91
BCUP_switch = 92
BCDN_switch = 93
LCUP_switch = 94
LCDN_switch = 95

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
print 'set pin modes'
# set the pin mode to an input, 0, for all our switches
wiringpi.pinMode(73,0) #rup switch
wiringpi.pinMode(74,0) #Rdown
wiringpi.pinMode(75,0) #Vup
wiringpi.pinMode(76,0) #Vdown
wiringpi.pinMode(77,0) #Hup
wiringpi.pinMode(90,0) #HCup
wiringpi.pinMode(91,0) #HCDown
wiringpi.pinMode(78, 0) #bup
wiringpi.pinMode(92, 0) #BCup
wiringpi.pinMode(93, 0) #BCdown
wiringpi.pinMode(89, 0) #Lup
wiringpi.pinMode(94, 0) #VCup
wiringpi.pinMode(95, 0) #LCdwn


# the mcp23017 ic has an internal pull up resistor. enabling this will keep the output pulled high. this stops any floating states which could cause odd things to happen in our script, 2
wiringpi.pullUpDnControl(73,2)
# ~ wiringpi.pullUpDnControl(RDN_switch,2)
# ~ wiringpi.pullUpDnControl(VSUP_switch,2)
# ~ wiringpi.pullUpDnControl(VSDN_switch,2)
# ~ wiringpi.pullUpDnControl(HUP_switch,2)
# ~ #wiringpi.pullUpDnControl(HDown_switch,2)
# ~ wiringpi.pullUpDnControl(HCUP_switch,2)
# ~ wiringpi.pullUpDnControl(HCDN_switch,2)
# ~ wiringpi.pullUpDnControl(BUP_switch,2)
# ~ wiringpi.pullUpDnControl(BCUP_switch,2)
# ~ wiringpi.pullUpDnControl(BCDN_switch,2)
# ~ wiringpi.pullUpDnControl(LUP_switch,2)
# ~ wiringpi.pullUpDnControl(LCUP_switch,2)
# ~ wiringpi.pullUpDnControl(LCDN_switch,2)
print 'done setting pin modes'
#Ok Set up the LED pin IDs
#Reactor
# ~ R1 = 17 #Note R1, H1, B1 and L1 are always on and use 3.3v pin 17
# ~ R2 = 3
# ~ R3 = 5
# ~ R4 = 7
# ~ R5 = 8
# ~ R6 = 10
# ~ R7 = 11

# ~ #Voids
# ~ V1 = 11
# ~ V2 = 13
# ~ V3 = 15
# ~ V4 = 16
# ~ V5 = 18
# ~ V6 = 19

# ~ #Head
# ~ H1 = 17
# ~ H2 = 21
# ~ H3 = 22
# ~ H4 = 23
# ~ H5 = 24
# ~ H6 = 26
# ~ H7 = 29

# ~ #Head Criticals
# ~ HC1 = 31
# ~ HC2 = 32
# ~ HC3 = 33

# ~ #Body
# ~ B1 = 17
# ~ B2 = 36
# ~ B3 = 37
# ~ B4 = 38
# ~ B5 = 39
# ~ B6 = 65
# ~ B7 = 66
# ~ B8 = 67

# ~ #Body Criticals
# ~ BC1 = 68
# ~ BC2 = 69
# ~ BC3 = 70

# ~ #Legs
# ~ L1 = 17
# ~ L2 = 81
# ~ L3 = 82
# ~ L4 = 83
# ~ L5 = 84
# ~ L6 = 85
# ~ L7 = 86
# ~ L8 = 87

# ~ #Legs Criticals
# ~ LC1 = 71
# ~ LC2 = 72
# ~ LC3 = 88

print 'setup pins'

#Set Reactor LED GPIO
GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(5 ,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(7 ,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(8 ,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(10,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(11,GPIO.OUT, initial=GPIO.LOW)

#Set Void Sheild LED GPIO
GPIO.setup(11,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(13,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(15,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(18,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(19,GPIO.OUT, initial=GPIO.LOW)

#Set Head LED GPIO
GPIO.setup(21,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(23,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(24,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(29,GPIO.OUT, initial=GPIO.LOW)

#Set Head Crit LED GPIO
GPIO.setup(31,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(32,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(33,GPIO.OUT, initial=GPIO.LOW)

I = 1
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
    print 'In the loop ' + str(I)
    print 'wipi ' +str(wiringpi.digitalRead(73))
    I = I + 1 


	
	#If a press happens I compare states and if it has gone low to high change my led state
    # ~ if not wiringpi.digitalRead(73):
	    # ~ if PRUp =='Open':
                # ~ PRUp = 'Closed'
                # ~ PRUPSC = 1
            # ~ else:
			   # ~ PRUPSC = 0
			   
    # ~ if not wiringpi.digitalRead(RDN_switch):
            # ~ if PRDown =='Open':
                # ~ PRDown = 'Closed'
                # ~ PRDNSC = 1
            # ~ else:
			   # ~ PRDNSC = 0
			   
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
    
    print 'in reactor'
    # ~ if Reactor == 1:
          # ~ GPIO.output(R2, GPIO.LOW)
          # ~ GPIO.output(R3, GPIO.LOW)
          # ~ GPIO.output(R4, GPIO.LOW)
          # ~ GPIO.output(R5, GPIO.LOW)
          # ~ GPIO.output(R6, GPIO.LOW)
	  # ~ GPIO.output(R7, GPIO.LOW)
				
    # ~ if Reactor == 2:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.LOW)
          # ~ GPIO.output(R4, GPIO.LOW)
          # ~ GPIO.output(R5, GPIO.LOW)
          # ~ GPIO.output(R6, GPIO.LOW)
	  # ~ GPIO.output(R7, GPIO.LOW)
	  
    # ~ if Reactor == 3:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.HIGH)
          # ~ GPIO.output(R4, GPIO.LOW)
          # ~ GPIO.output(R5, GPIO.LOW)
          # ~ GPIO.output(R6, GPIO.LOW)
	  # ~ GPIO.output(R6, GPIO.LOW)	  

    # ~ if Reactor == 4:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.HIGH)
          # ~ GPIO.output(R4, GPIO.HIGH)
          # ~ GPIO.output(R5, GPIO.LOW)
          # ~ GPIO.output(R6, GPIO.LOW)
	  # ~ GPIO.output(R7, GPIO.LOW)

    # ~ if Reactor == 5:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.HIGH)
          # ~ GPIO.output(R4, GPIO.HIGH)
          # ~ GPIO.output(R5, GPIO.HIGH)
          # ~ GPIO.output(R6, GPIO.LOW)
	  # ~ GPIO.output(R7, GPIO.LOW)
	  
    # ~ if Reactor == 6:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.HIGH)
          # ~ GPIO.output(R4, GPIO.HIGH)
          # ~ GPIO.output(R5, GPIO.HIGH)
          # ~ GPIO.output(R6, GPIO.HIGH)
	  # ~ GPIO.output(R7, GPIO.LOW)	  
	  
    # ~ if Reactor == 7:
          # ~ GPIO.output(R2, GPIO.HIGH)
          # ~ GPIO.output(R3, GPIO.HIGH)
          # ~ GPIO.output(R4, GPIO.HIGH)
          # ~ GPIO.output(R5, GPIO.HIGH)
          # ~ GPIO.output(R6, GPIO.HIGH)
	  # ~ GPIO.output(R7, GPIO.HIGH)	  
	  	  
    # ~ #print wiringpi.digitalRead(blue_switch)    
    # ~ if wiringpi.digitalRead(RUP_switch):
        # ~ PRUp = 'Open'
        # ~ PRUPSC = 0
    # ~ if wiringpi.digitalRead(RDN_switch):
        # ~ PRDown = 'Open'
        # ~ PRDNSC = 0
	
	# ~ #Begin Void Sheild Block
    # ~ if not wiringpi.digitalRead (VSUP_switch):
	    # ~ if VSUp =='Open':
                # ~ VSUp = 'Closed'
                # ~ VSUPSC = 1
            # ~ else:
			   # ~ VSUPSC = 0
			   
    # ~ if not wiringpi.digitalRead(VSDN_switch):
            # ~ if VSDown =='Open':
                # ~ VSDown = 'Closed'
                # ~ VSDNSC = 1
            # ~ else:
			   # ~ VSDNSC = 0

    # ~ #print "VSup " + str(VSUp) + " VSDown " + str(VSDown) 
    
    # ~ if VSUPSC == 1 and VSDNSC == 0:
		# ~ if Voids > 0 and Voids < 6:
			# ~ Voids = Voids + 1

		# ~ print "Voids " + str(Voids) 
			 
    # ~ if VSUPSC == 0 and VSDNSC == 1:
		# ~ if Voids > 1 and Voids <= 6:
			# ~ Voids = Voids - 1


		# ~ print "Voids " + str(Voids)
			 
    # ~ if VSDown == 'Closed' and VSUp == 'Closed':
            # ~ VSBothCount = VSBothCount +1
    # ~ else:
	    # ~ VSBothCount = 0
    
    # ~ if VSBothCount == 100:
		# ~ if Voids > 0 :
		  # ~ Voids = -1
		# ~ else:
		  # ~ Voids = 6
  # ~ #  print "voids: " + str(Voids) + " VSup " + str(VSUp) + " VSDown " + str(VSDown) + " VSUPSC " + str(VSUPSC) +  " VSDNSC " + str(VSDNSC)
  # ~ #  print "bothCount: " + str(VSBothCount)
    
    # ~ print 'In voids'
    # ~ if Voids == -1:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.LOW)
 
    # ~ if Voids == 1:
       # ~ GPIO.output(V1, GPIO.HIGH)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.LOW)
       
    # ~ if Voids == 2:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.HIGH)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.LOW)
  
    # ~ if Voids == 3:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.HIGH)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.LOW)
 
    # ~ if Voids == 4:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.HIGH)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.LOW)
       
    # ~ if Voids == 5:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.HIGH)
       # ~ GPIO.output(V6, GPIO.LOW)
       
    # ~ if Voids == 6:
       # ~ GPIO.output(V1, GPIO.LOW)
       # ~ GPIO.output(V2, GPIO.LOW)
       # ~ GPIO.output(V3, GPIO.LOW)
       # ~ GPIO.output(V4, GPIO.LOW)
       # ~ GPIO.output(V5, GPIO.LOW)
       # ~ GPIO.output(V6, GPIO.HIGH) 
  
    
    # ~ if wiringpi.digitalRead(VSUP_switch):
        # ~ VSUp = 'Open'
        # ~ VSUPSC = 0
    # ~ if wiringpi.digitalRead (VSDN_switch):
        # ~ VSDown = 'Open'
        # ~ VSDNSC = 0

# ~ ##Head Tracker
    # ~ print "Switch state " + str(wiringpi.digitalRead(HUP_switch))
    # ~ if not wiringpi.digitalRead(HUP_switch):
	    # ~ if HUp =='Open':
                # ~ HUp = 'Closed'
                # ~ HUPSC = 1

            # ~ else:
		# ~ HUPSC = 0

			   
   
    
    # ~ if HUPSC == 1: #and HDNSC == 0:
         # ~ if Head < 8: 
	      # ~ Head = Head + 1
         # ~ elif Head > 7: 
	      # ~ Head = 1
    # ~ print 'In head'
    # ~ if Head == 1:
        # ~ GPIO.output(H2, GPIO.LOW)
	# ~ GPIO.output(H3, GPIO.LOW)
	# ~ GPIO.output(H4, GPIO.LOW)
	# ~ GPIO.output(H5, GPIO.LOW)
	# ~ GPIO.output(H6, GPIO.LOW)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 2:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.LOW)
	# ~ GPIO.output(H4, GPIO.LOW)
	# ~ GPIO.output(H5, GPIO.LOW)
	# ~ GPIO.output(H6, GPIO.LOW)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 3:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.HIGH)
	# ~ GPIO.output(H4, GPIO.LOW)
	# ~ GPIO.output(H5, GPIO.LOW)
	# ~ GPIO.output(H6, GPIO.LOW)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 4:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.HIGH)
	# ~ GPIO.output(H4, GPIO.HIGH)
	# ~ GPIO.output(H5, GPIO.LOW)
	# ~ GPIO.output(H6, GPIO.LOW)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 5:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.HIGH)
	# ~ GPIO.output(H4, GPIO.HIGH)
	# ~ GPIO.output(H5, GPIO.HIGH)
	# ~ GPIO.output(H6, GPIO.LOW)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 6:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.HIGH)
	# ~ GPIO.output(H4, GPIO.HIGH)
	# ~ GPIO.output(H5, GPIO.HIGH)
	# ~ GPIO.output(H6, GPIO.HIGH)
	# ~ GPIO.output(H7, GPIO.LOW)
	
    # ~ if Head == 7:
        # ~ GPIO.output(H2, GPIO.HIGH)
	# ~ GPIO.output(H3, GPIO.HIGH)
	# ~ GPIO.output(H4, GPIO.HIGH)
	# ~ GPIO.output(H5, GPIO.HIGH)
	# ~ GPIO.output(H6, GPIO.HIGH)
	# ~ GPIO.output(H7, GPIO.HIGH)

	      
	      
    
    
 
    # ~ if wiringpi.digitalRead(HUP_switch):
        # ~ HUp = 'Open'
        # ~ HUPSC = 0
 	
 
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
#sleep(0.1)
