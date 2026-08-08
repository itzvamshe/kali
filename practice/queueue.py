# queue using list [] O(1) 

q = []
q.append('a')
q.append('b')
q.append('c')

print("Initial queue: ",q)

print("Elements dequeue from queue:")
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

print("Queue after removing elements: ",q)

# queue using collections dequeue [ double ended queue)

from collections import deque

q = deque()

q.append('a')
q.append('b')
q.append('c')

print("Initial queue:",q)

print("Elements dequed from the queue:")

print(q.popleft())
print(q.popleft())
print(q.popleft())

print("Queue after removing elements :",q)

# queue using queue.Queue

from queue  import Queue

q = Queue(maxsize=3)

print("Initial size:",q.qsize())

q.put('a')
q.put('b')
q.put('c')

print("Is full: ",q.full())
print("Elements dequeued from the queue:")
print(q.get())
print(q.get())
print(q.get())
print("Is empty:",q.empty())
q.put(1)
print("Is empty:",q.empty())
print("is full:",q.full())

