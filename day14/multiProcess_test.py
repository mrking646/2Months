from multiprocessing import Process
import time

def f(name):
    time.sleep(1)
    print("hello", name, time.ctime())

if __name__ == "__main__":
    p_list = []
    for i in range(3):

        p = Process(target=f, args=('alvin',))
        p_list.append(p)
        p.start()

    for i in p_list:
        i.join()

    print("end")
    
