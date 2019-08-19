class Room:
    def __init__(self, name, owner, width, length, height):
        self.name = name
        self.owner = owner
        self.width = width
        self.length = length
        self.height = height
    @property
    def cal_area(self):
        print("%s has a %s take %s" % (self.owner, self.name, self.width*self.length))


r1 = Room('house', 'owner', 100, 100, 1000)
print(r1.cal_area)