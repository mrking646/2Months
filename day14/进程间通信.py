import multiprocessing
import time


def foo(q):
    time.sleep(1)
    print("son process", id(q))
    q.put(123)
    q.put("hello")

if __name__ == "__main__":

    q = multiprocessing.Queue()

    p = multiprocessing.Process(target=foo, args=(q,))

    p.start()
    p.join()

    print("main process", id(q))
    print(q.get())
    print(q.get())