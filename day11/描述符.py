class Typed:

    def __init__(self, key, expected_type):
        self.key = key
        self.expected_type = expected_type


    def __get__(self, instance, owner):
        print('get 方法')
        print('instance 参数[%s]' % instance)
        print('owner 参数[%s]' % owner)
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        print('set 方法')
        print('instance 参数[%s]' % instance)
        print('value 参数 [%s]' % value)
        if not isinstance(value, self.expected_type):
            raise TypeError("传入类型必须为%s" % self.expected_type)
        instance.__dict__[self.key] = value


class People:
    name = Typed('name', str)
    age = Typed('age', int)

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

p1 = People('ss', 'he', 1)