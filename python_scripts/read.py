import sys
import pdb
import testing
import datetime
from datetime import time
from datetime import timedelta
import RPi.GPIO as GPIO

class TimeReader:
    #initialize for each new object
    def __init__(self):
        self.durations = []  #empty list for signal durations
        self.lastTime = datetime.datetime.now().time()   #current time

    #a function to run on a different thread when a change in channel's input value is detected
    def edgeDetectionCallback(self, channel):
        self.thisTime = datetime.datetime.now().time()

        self.lastTimeDelta = timedelta(seconds=self.lastTime.second, microseconds=self.lastTime.microsecond)
        self.thisTimeDelta = timedelta(seconds=self.thisTime.second, microseconds=self.thisTime.microsecond)

        self.durations.append((self.thisTimeDelta - self.lastTimeDelta).microseconds)
        self.lastTime = self.thisTime

    #prints lengths of time the input signal spends high or low
    #assumes signal begins as high and disregards first duration
    #assumes the user holds the button down sufficiently long
    def printTimes(self, deviceName, cmdName):
        #sets up GPIO pins
        testing.irSetup()

        #adds interrupt on input pin changing value
        GPIO.add_event_detect(15, GPIO.BOTH, callback=self.edgeDetectionCallback)

        #waits until keyboard interrupt
        try:
            while (len(self.durations) < 51):        #wait until 51 durations are stored
                pass
        except KeyboardInterrupt:
            pass

        #resets GPIO pins to default states
        GPIO.cleanup()
        
        #opens file and appends to it.
        #will create file if it doesn't already exist
        self.file = open(deviceName + ".txt", "a+")

        #write name of command
        self.file.write(cmdName + "\r\n")
        
        #writes signal durations to file, skipping first
        for i in range(1, len(self.durations)):
            self.file.write(str(self.durations[i]) + "\r\n")

        self.file.write("\r\n")

        self.file.close()


def write(deviceName, cmdName):
    #create a new instance of the TimeReader class.
    #the __init__ method is called automatically
    tr = TimeReader()

    #read and print signal durations
    tr.printTimes(deviceName, cmdName)

    #instance should be deleted when it goes out of scope

if __name__ == "__main__":
    deviceName = sys.argv[1]
    cmdName = sys.argv[2]
    write(deviceName, cmdName)
    
