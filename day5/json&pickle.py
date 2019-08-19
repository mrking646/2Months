import json
#
# # dic = {"name": "zhenji"}
# #
# # data = json.dumps(dic)
# # f = open("new_hello", "w")
# # f.write(data)
#
# f_read = open("new_hello", "r")
# data = json.loads(f_read.read())
# print(data)
# print(type(data))

import json

with open("new_hello", "r") as f:
    data = f.read()
    data = json.loads(data)
    print(data["name"])