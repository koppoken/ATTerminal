#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep

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
# enable ic2 on the mcp23017 hat
wiringpi.mcp23017Setup(ic2_pin_base,ic2_i2c_addr)

# use pin 1 on IC1
led = 65
# use pin 1 on IC2
switch = 81

# set the pin mode to an output, 1
wiringpi.pinMode(led,1)
# set the pin to off, 0
wiringpi.digitalWrite(led,0)

# set the pin mode to an input, 0
wiringpi.pinMode(switch,0)
# the mcp23017 ic has an internal pull up resistor. enabling this will keep the output pulled high. this stops any floating states which could cause odd things to happen in our script, 2
wiringpi.pullUpDnControl(switch,2)

# create an infinite loop
while True:
	# because we set the pull up resistor on our output, when we press the button the pin state will actually go low. so we need to check when the pin is low 
	if not wiringpi.digitalRead(switch):
		wiringpi.digitalWrite(led,1)
	# when we release the button the pin state changes back to high
	else:
		wiringpi.digitalWrite(led,0)
	print "running"
# add a little pause for 1/10 of a second, to allow other process on the Pi to happen, we dont want to hog all the cpu :)
sleep(0.1)
