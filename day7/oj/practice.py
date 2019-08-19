def school(name, addr, type):
    def recruit(school):
        print("%s %s is recruiting" % (school['type'], school['name']))

    def having_exam(school):
        print("%s %s is having an exam" % (school['type'], school['name']))

    def init(name, addr, type):
        sch = {
            "name": name,
            "type": type,
            "addr": addr,
            "recruit": recruit,
            "having_exam": having_exam,
        }
        return sch
    return init(name, addr, type)


s1 = school("Neusoft", "Dalian", "Private")
print(s1)
s1["recruit"](s1)