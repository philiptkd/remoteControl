#TODO
#   wrap with a class
#   make callback function a class method
#   create new instance of class with each call to wrapper function
#   make global variables instance variables
#   destroy instance of class at end of wrapper function (already done automatically?)

import testing
import datetime
from datetime import time
from datetime import timedelta
import RPi.GPIO as GPIO

#create list to hold time values
durations = []
lastTime = datetime.datetime.now().time()

#a function to run on a different thread when a change in channel's input value is detected
def edgeDetectionCallback(channel):
    global lastTime, durations

    thisTime = datetime.datetime.now().time()

    lastTimeDelta = timedelta(seconds=lastTime.second, microseconds=lastTime.microsecond)
    thisTimeDelta = timedelta(seconds=thisTime.second, microseconds=thisTime.microsecond)

    durations.append((thisTimeDelta - lastTimeDelta).microseconds)
    lastTime = thisTime

#prints lengths of time the input signal spends high or low
#assumes signal begins as high and disregards first duration
#assumes the user holds the button down sufficiently long
def printTimes():
    #sets up GPIO pins
    testing.irSetup()

    #adds interrupt on input pin changing value
    GPIO.add_event_detect(15, GPIO.BOTH, callback=edgeDetectionCallback)

    #waits until keyboard interrupt
    try:
        while (len(durations) < 51):        #wait until 51 durations are stored
            pass
    except KeyboardInterrupt:
        pass

    #resets GPIO pins to default states
    testing.irClose()
    
    #prints durations of signal. the first value is garbage
    for i in range(1, len(durations)):
        print("%d" % (durations[i]))
