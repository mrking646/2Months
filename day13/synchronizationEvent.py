import threading, time

class Boss(threading.Thread):
    def run(self):
        print("BOSS: today we will work till 22:00.")
        print(event.isSet())
        event.set()
        time.sleep(5)
        print("BOSS: <22:00> let's go")
        print(event.isSet())
        event.set()


class Worker(threading.Thread):

    def run(self):
        event.wait() # once the event was setted, go on
        print("Worker: life is hard\n")
        time.sleep(1)
        event.clear()
        event.wait()
        print("Worker: Yeah!\n")


if __name__ == "__main__":
    event = threading.Event()


    threads = []

    for i in range(5):
        threads.append(Worker())

    threads.append(Boss())
    for t in threads:
        t.start()

    for t in threads:
        t.join()
