def dog(name, gender, type):

    def bark(dog):
        print("a dog[%s], wang, wang, wang" % dog['name'])

    def eat(dog):
        print("a dog[%s] was eating" % dog['type'])

    def init(name, gender, type):
        dog1 = {
            'name': name,
            'gender': gender,
            'type': type,
            'bark': bark,
            'eat': eat,
        }
        return dog1

    res = init(name, gender, type)

    return res





d1 = dog('zhenji', 'male', 'husky')
print(d1)
d1['bark'](d1)