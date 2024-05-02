import RPi.GPIO as GPIO 
PIR_input = 8 
LED = 10 
GPIO.setwarnings (False) 
GPIO.setmode (GPIO.BOARD) 
GPIO.setup(PIR_input, GPIO.IN) 
GPIO.setup(LED, GPIO.OUT) 
GPIO.output (LED, GPIO.LOW) 
while True: 
      if(GPIO.input (PIR_input)): 
           print("Detected") 
           GPIO.output(LED, GPIO.HIGH) 
      else: 
           GPIO.output(LED, GPIO.LOW) 
           print("not detected") 