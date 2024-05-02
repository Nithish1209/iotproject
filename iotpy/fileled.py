import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
x =open("filename.txt","r")
for line in x:
    print(line)
s=int(line[0])
end=int(line[2])
print("strats at:",s,"ends at : ",end)
try:
    while(True):
        GPIO.output(8,True)
        time.sleep(s)
        GPIO.output(8,False)
        time.sleep(end)
        print("*")
finally:
    GPIO.output(8,False)
    GPIO.cleanup()