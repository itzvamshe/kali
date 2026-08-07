# List implementation.

list_stack = []

list_stack.append("a")
list_stack.append("b")
list_stack.append("c")

print(list_stack)
print(list_stack.pop())
print(list_stack.pop())

# collections.deque
from collections import deque

deque_stack = deque()

deque_stack.append("a")
deque_stack.append("b")
deque_stack.append("c")

print(deque_stack)
print(deque_stack.pop())
print(deque_stack.pop())


# qeue.LifoQueue

from queue import LifoQueue

st = LifoQueue()

st.put("a")
st.put("b")
st.put("c")

print(st.get())
print(st.get())



