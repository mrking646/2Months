class Vehicle:
    def __init__(self, name, speed, load, power):
        self.name = name
        self.speed = speed
        self.load = load
        self.power = power

    def run(self):
        print("Let's go!")

class Subway(Vehicle):
    def __init__(self, name, speed, load, power, line):
        super(Subway, self).__init__(name, speed, load,power)
        self.line = line

    def run(self):
        super(Subway, self).run()
        print("%s %s line is about to running..." % (self.name, self.line))

metro13 = Subway("metro", 60, 1000, "eletric", "13")
print(metro13.run())