import shelve

f = shelve.open(r'shelve1')

f['stu1_info'] = {'name': 'zhenji', "age":12}
f['stu2_info'] = {'name': 'zhangsan', "age": 22}
f['sch_info'] = {"name": 'll'}
f.close()

