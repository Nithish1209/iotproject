import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.OUT)

for i in range(50):
    GPIO.output(10, True)
    print("LED is ON")
    time.sleep(0.1)
    GPIO.output(10, False)
    print("LED is OFF")
    time.sleep(0.1)

GPIO.cleanup()
