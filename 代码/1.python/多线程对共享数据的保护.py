from threading import Thread,Lock
import time



num = 0
def test1():
	global num
	mutex.acquire()
	for x in range(1000000):
		num += 1
	mutex.release()
	print("---test1---num=%d"%num)

def test2():
	global num
	mutex.acquire()
	for x in range(1000000):
		num += 1
	mutex.release()
	print("---test2---num=%d"%num)

mutex = Lock()

thread = Thread(target = test1)
thread.start()

#time.sleep(3)

thread = Thread(target = test2)
thread.start()