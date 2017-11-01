import RPi.GPIO as GPIO
    
def irSetup():
    #use the BOARD pin numbering system
    GPIO.setmode(GPIO.BOARD)

    #set pin 16 (GPIO 23) as an output
    GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

    #set pin 15 (GPIO 22) as an input
    GPIO.setup(15, GPIO.IN)    

def irClose():
    #resets pin configurations to defaults
    GPIO.cleanup([15, 16])

def testSend():
    #setup GPIO pins
    irSetup()

    #create a PWM instance on pin 16 with a frequency of 38kHz
    pwm = GPIO.PWM(16, 38000)

    #start the PWM with a duty cycle of 50
    pwm.start(50)

    #leave on until keyboard interrupt
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass

    #stop PWM. it would also stop if pwm went out of scope
    pwm.stop()

    irClose()      

def testReceive():
    #setup GPIO pins
    irSetup()

    try:
        while True:
            #print value from sensor
            print(GPIO.input(15))
    except KeyboardInterrupt:
        pass

    irClose()

def test():
    irSetup()

    #create a PWM instance on pin 16 with a frequency of 38kHz
    pwm = GPIO.PWM(16, 38000)

    #start the PWM with a duty cycle of 50
    pwm.start(50)

    #leave on until keyboard interrupt or sensor reads it
    try:
        while True:
            if (GPIO.input(15) == 0):
                print("All hardware is functioning normally.")
                break
    except KeyboardInterrupt:
        pass

    irClose()
