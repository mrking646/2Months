import multiprocessing

def f(l, n):

    with l:
        print("hello zhenji", n)



if __name__ == "__main__":
    l = multiprocessing.Lock()

    for num in range(10):

        multiprocessing.Process(target=f, args=(l, num)).start()