import threading
import time

num = 100


def sub_():
    global num

    lock.acquire()
    temp = num
    time.sleep(0.0001)
    num = temp - 1
    lock.release()

l = []
lock = threading.Lock()
for i in range(100):
    t = threading.Thread(target=sub_) 
    t.start()
    l.append(t)


for t in l:
    t.join()


print(num)