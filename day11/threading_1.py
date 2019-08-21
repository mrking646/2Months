import threading
import time

def music():
    print("begin to listen music ", time.ctime())
    time.sleep(3)
    print("stop to listen music", time.ctime())

def game():
    print("begin to play game", time.ctime())
    time.sleep(5)
    print("stop to play game", time.ctime())

if __name__ == "__main__":

    t1 = threading.Thread(target=music)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=game)
    t2.start()

    t2.join()
    print("\nending")
