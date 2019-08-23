import queue

q = queue.Queue(3)

q.put(12)
q.put("hello")
q.put({"name": "zhenji"})
q.put(111, False)
while q:
    data = q.get()
    print(data)
    print("="*10,">")