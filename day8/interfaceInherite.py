import abc

class All_file(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractmethod
    def write(self):
        pass


class Disk(All_file):

    def read(self):
        print("Disk read")

    def write(self):
        print("Disk write")

class CDrom(All_file):

    def read(self):
        print("CD read")

    def write(self):
        print("CD write")

class Mem(All_file):

    def read(self):
        print("CD read")

    def write(self):
        print("CD write")

m1 = Mem()
