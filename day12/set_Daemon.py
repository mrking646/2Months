import threading
from time import ctime, sleep
import time

def listen_music():
    print("begin to listen to music ", time.ctime())
    sleep(3)
    print("end listening", time.ctime())

def RecordBlog():
    print("begin to record a blog"+time.ctime()+ "\n")
    sleep(5)
    print("end recording", time.ctime())

threads = []

t1 = threading.Thread(target=listen_music,)
t2 = threading.Thread(target=RecordBlog,)

threads.append(t1)
threads.append(t2)

if __name__ == "__main__":
    t2.setDaemon(True)
    for t in threads:
        t.start()

    print("all over!!!!", time.ctime())