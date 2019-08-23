from multiprocessing import Process
import os
import time

def info(title):
    print("title", title)
    print("parent process", os.getppid())
    print("process id", os.getpid())

def f(name):
    info("function f")
    print("hello", name)

if __name__ == "__main__":

    info("main process line")

    time.sleep(1)
    print("-"*20)
    p = Process(target=info, args=("zhenji",))
    p.start()
    p.join()