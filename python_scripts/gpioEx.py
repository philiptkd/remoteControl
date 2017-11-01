import RPi.GPIO as GPIO

#use the BOARD pin numbering system
#GPIO.setmode(GPIO.BOARD)

############### START SIMPLE ##################
#set pin 15 (GPIO 22) as an input
#GPIO.setup(15, GPIO.IN)      

#set pin 16 (GPIO 23) as an output
#GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

#read the value of an input pin
#GPIO.input(pinNumber)

#set the value of an output pin, where value is 0 or 1
#GPIO.output(pinNumber, value)
################ END SIMPLE ###################

############### START PWM ##################
#set pin 16 (GPIO 23) as an output
#GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)

#create a PWM instance on pin 16 with a frequency of 38kHz
#pwm = GPIO.PWM(16, 38000)

#start the PWM with a duty cycle of 0
#pwm.start(0)

#change duty cycle to 50%
#pwm.ChangeDutyCycle(50)

#stop PWM. it would also stop if pwm went out of scope
#pwm.stop()
################ END PWM ###################

#GPIO.cleanup([15, 16])      #resets pin configurations to defaults
