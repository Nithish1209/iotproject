import time 
import adafruit_dht 
import board 
dht_device = adafruit_dht.DHT22(board.D15) 
while True: 
    try: 
        t_c = dht_device.temperature 
        t_f = t_c * (9 / 5) + 32 
        h = dht_device.humidity 
        print(t_c, t_f, h) 
    except RuntimeError as err: 
        print(err.args[0]) 
    time.sleep(2.0) 