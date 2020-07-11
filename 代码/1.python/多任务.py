import os
import time
ret = os.fork()
if ret == 0:
	while True:
		print("1")
		sleep(1)
else:
	while True:
		print("2")
		sleep(1)