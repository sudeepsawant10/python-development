import queue
q = queue.Queue(maxsize=6)
for i in range(4):
    q.put(i)

while not q.empty():
    print(q.get())
