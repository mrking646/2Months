class School:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

    def recruit(self):
        print("%s is recruiting" % self.name)


class Course:

    def __init__(self, name, price, period, school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school


s1 = School("oldboy", "beijing")
s2 = School("oldboy", "nanjing")

c1 = Course('Linux', 10, '1h', s1)

# print(c1.__dict__)
# print(c1.school.name)

msg = """
    1: oldboy beijing
    2: oldboy nanjing
    3: oldboy tokyo
"""

while True:
    print(msg)
    menu = {
        '1': s1,
        '2': s2,
    }

    choice1 = input(">>: ")
    school_obj = menu[choice1]

    name = input("new subject>> ")
    price = input("price>> ")
    period = input("period>> ")

    new_course = Course(name, price, period, school_obj)
    print("course %s belong to %s school" % (new_course.name, new_course.school.name))

print(Course.__dict__)

# class Hand:
#     pass
#
# class Foot:
#     pass
#
# class Trunk:
#     pass
#
# class Head:
#     pass
#
#
#
#
# class Person:
#
#
#     def __init__(self, id_num, name):
#         self.id_num = id_num
#         self.name = name
#         self.hand = Hand()
#         self.foot = Foot()
#         self.Trunk = Trunk()
#         self.head = Head()
#
# p1 = Person("111", 'zhenji')
# print(p1.__dict__)
