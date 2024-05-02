import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
s1=18
s2=24
l1=23
l2=25
GPIO.setup(s1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(l2,GPIO.OUT)
try:
    while True:

            if GPIO.input(switch1_pin) == GPIO.LOW:
               print("Switch 1 pressed. Turning on LED 1.")
               GPIO.output(led1_pin, GPIO.HIGH)
            else:
                GPIO.output(led1_pin, GPIO.LOW)
   
            if GPIO.input(switch2_pin) == GPIO.LOW:
                print("Switch 2 pressed. Turning on LED 2.")
                GPIO.output(led2_pin, GPIO.HIGH)
            else:
                GPIO.output(led2_pin, GPIO.LOW)
except KeyboardInterrupt:
      print("Exiting program.")
      GPIO.cleanup()

