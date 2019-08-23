from multiprocessing import Process, Pool
import time, os


def Foo(i):
    time.sleep(1)
    print(i)
    print("Foo", os.getpid())


def Bar(arg):
    print("hello")
    print("bar", os.getpid())



if __name__ == "__main__":
    pool = Pool()
    print("main pid", os.getpid())
    for i in range(100):
        pool.apply_async(func=Foo, args=(i,), callback=Bar)


    pool.close()
    pool.join()
    print("end")