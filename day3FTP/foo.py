def father(name):
    print("from father %s " % name)
    def son():
        pass
    print(locals())

father('zhenji')