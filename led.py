#!/usr/bin/python

import wiringpi as wiringpi
from time import sleep

# set the base number of ic1, this can be any number above (not including) 64
ic1_pin_base = 65
# pin number to code number:
# 1 = 65, 2 = 66, 3 = 67, 4 = 68, 5 = 69, 6 = 70, 7 = 71, 8 = 72, 9 = 73, 10 = 74, 11 = 75, 12 = 76, 13 = 77, 14 = 78, 15 = 79, 16 = 80
# define the i2c address of ic1, this is set by the jumpers on the HAT
ic1_i2c_addr = 0x24

# initiate the wiringpi library
wiringpi.wiringPiSetup()
# enable ic1 on the mcp23017 hat
wiringpi.mcp23017Setup(ic1_pin_base,ic1_i2c_addr)

# use pin 1 on IC1
led = 65

# set the pin mode to an output, 1
wiringpi.pinMode(led,1)
# set the pin to off, 0
wiringpi.digitalWrite(led,0)

# create an infinite loop
while True:
	# set the pin to on, 1
	wiringpi.digitalWrite(led,1)
	# wait 0.5 seconds
	sleep(0.5)
	# set the pin to off, 0
	wiringpi.digitalWrite(led,0)
	# wait 0.5 seoncds
	sleep(0.5)