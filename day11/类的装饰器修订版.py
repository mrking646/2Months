def Typed(**kwargs):


    def deco(obj):
        print('--->', kwargs)
        print('class name--->', obj)
        for key, val in kwargs.items():

            setattr(obj, key, val)
        return obj

    print("==>", kwargs)
    return deco

@Typed(x =1 , y = 2)
class Foo:
    pass

print(Foo.__dict__)

@Typed(name = "zhenji")
class Bar:
    pass

print(Bar.__dict__)