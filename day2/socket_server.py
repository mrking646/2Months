from functools import partial

def add(x, y):
    return x + y

func = partial(add, 1)
print(func(20))