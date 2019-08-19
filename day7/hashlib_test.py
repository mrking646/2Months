import hashlib

obj=hashlib.md5("admin".encode("utf8"))

obj.update("hello".encode("utf8"))

print(obj.hexdigest())