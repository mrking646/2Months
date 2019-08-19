user_list = [
    {'username': 'zhenji', 'passwd':'123'},
    {'username': 'zhangsan', 'passwd':'123'},
    {'username': 'lisi', 'passwd':'123'},
]

current_id = {'username': None, 'login': False}

def auth(func):
    def wrapper(*args, **kwargs):
        if current_id['username'] and current_id['login']:
            res = func(*args, **kwargs)
            return res

        username = input('username: ')
        passwd = input("password: ")

        for user_dict in user_list:
            if username == user_dict['username'] and passwd == user_dict['passwd']:
                current_id['username'] = username
                current_id['login'] = True
                res = func(*args, **kwargs)
                return res

        else:
            print("wrong username or password!")

    return wrapper





@auth
def index():
    print('welcome to the index')

@auth
def home(name):
    print('welcome to home, %s' % name)

@auth
def shopping_car(name):
    print("%s's shopping car has %s %s"%(name, '1', '2'))

index()
home("zhenji")
shopping_car('zhenji')