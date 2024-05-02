import RPi.GPIO as GPIO
import time
import os, sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(35, GPIO.OUT)      
GPIO.setup(12, GPIO.OUT)      
GPIO.setup(36, GPIO.OUT)      
GPIO.setup(33, GPIO.OUT)      
GPIO.setup(32, GPIO.OUT)      
GPIO.setup(38, GPIO.OUT)      
GPIO.setup(40, GPIO.OUT)      

digitclr=[1,1,1,1,1,1,1]
digit0=[0,0,0,0,0,0,1]
digit1=[1,0,0,1,1,1,1]
digit2=[0,0,1,0,0,1,0]
digit3=[0,0,0,0,1,1,0]
digit4=[1,0,0,1,1,0,0]
digit5=[0,1,0,0,1,0,0]
digit6=[0,1,0,0,0,0,0,]
digit7=[0,0,0,1,1,1,1]
digit8=[0,0,0,0,0,0,0]
digit9=[0,0,0,1,1,0,0,]
gpin=[35,12,36,33,32,38,40]
 
def digdisp(digit):
    for x in range (0,7):
        GPIO.output(gpin[x], digitclr[x])
    for x in range (0,7):
        GPIO.output(gpin[x], digit[x])
 
digdisp(digit0)
time.sleep(1)
digdisp(digit1)
time.sleep(1)
digdisp(digit2)
time.sleep(1)
digdisp(digit3)
time.sleep(1)
digdisp(digit4)
time.sleep(1)
digdisp(digit5)
time.sleep(1)
digdisp(digit6)
time.sleep(1)
digdisp(digit7)
time.sleep(1)
digdisp(digit8)
time.sleep(1)
digdisp(digit9)
time.sleep(1)
GPIO.cleanup()
sys.exit()