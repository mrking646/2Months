class Open:

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print("execute enter")

    def __exit__(self,):