import time
 # Iterate 10 times to print the current time
for i in range(1, 11):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f"Iteration {i}: Current Time - {current_time}")

        time.sleep(10)