class Chinese:


    country='China'

    def __init__(self, name):
        self.name = name

    def play_ball(self, ball):
        print('%s is playing %s' %(self.name, ball))

p1 = Chinese('zhenji')
print(p1.country)

p1.country = "Japan"
print("class's--->", Chinese.country)
print("Instance's--->", p1.country)