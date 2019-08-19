def deco(obj):
    obj.x = 1
    obj.y = 2
    return obj

@deco
class Foo:
    pass

print(Foo.__dict__)