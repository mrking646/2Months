import threading
import time

class MyThread(threading.Thread):


    def actionA(self):
        r_lock.acquire()
        print(self.name, "got lockA", time.ctime())
        time.sleep(2)


        r_lock.acquire()
        print(self.name, "got lockB", time.ctime())

        r_lock.release()
        r_lock.release()

    def actionB(self):
        r_lock.acquire()
        print(self.name, "got lockB", time.ctime())
        time.sleep(2)

        r_lock.acquire()
        print(self.name, "got lockA", time.ctime())
        time.sleep(1)

        r_lock.release()
        r_lock.release()


    def run(self):
        self.actionA()
        self.actionB()









if __name__ == "__main__":

    l= []
    r_lock = threading.RLock()
    # A = threading.Lock()
    # B = threading.Lock()

    for i in range(5):
        t = MyThread()
        t.start()
        l.append(t)

    for i in l:
        i.join()