class Typed:

    def __init__(self, key, expected_type):
        self.key = key
        self.expected_type = expected_type


    def __get__(self, instance, owner):

        return instance.__dict__[self.key]

    def __set__(self, instance, value):

        if not isinstance(value, self.expected_type):
            raise TypeError("传入类型必须为%s" % self.expected_type)
        instance.__dict__[self.key] = value


def deco(**kwargs):
    def wrapper(obj):
        for key, val in kwargs.items():
            print("==>", key, val)
            setattr(obj, key, Typed(key, val))

        return obj
    return wrapper


@deco(name = str)
class People:


    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p1 = People('zhenji', 'he', 1)