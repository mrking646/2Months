from multiprocessing import Process, Manager

def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    l.append(n)
    print("son process: ", id(d), id(l))

if __name__ == "__main__":

    with Manager() as manager:

        d = manager.dict()

        l = manager.list(range(5))

        print("main process:", id(d), id(l))

        p_list = []

        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)