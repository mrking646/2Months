import time

def timmer(func):
    def wrapper():
        start_time = time.time()
        func()
        stop_time = time.time()
        print("函数的运行时间是 %s" %(stop_time-start_time))
    return wrapper

@timmer
def test():
    time.sleep(3)

test()

