import threading
import time

def add_1000000():
    sum = 0
    for i in range(1000000):
        sum += i

    return sum

def multi_1000000():
    products = 0
    for i in range(1,1000000):
        products *= i
    return products

def print1():
    print(add_1000000())

def print2():
    print(multi_1000000())

t1 = threading.Thread(target=print1)
t2 = threading.Thread(target=print2)
threads = []
if __name__ == "__main__":
    # time1 = time.time()
    # for t in threads:
    #     t.start()
    # time2 = time.time()
    # print("run time is ",(time2-time1))
    # print("all over!")
    time1 = time.time()
    print1()
    print2()
   
    time2 = time.time()
    print("run time is ",(time2-time1))