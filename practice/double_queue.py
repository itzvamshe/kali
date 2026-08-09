from collections import deque

d = deque(['name','age','DOB'])

print(d)

# accessing elements
print(d[0]) # access first element
print(d[-1]) # access last element

# operations on deque
# append() / appendleft(), extend() / extendleft() , remove() , pop() / popleft() , clear() , len() , count() , rotate() , reverse()

dq = deque([10,20,30])
dq.append(40)
print('appended: ',dq)

dq.appendleft(5)
print('leftappended: ',dq)

dq.extend([50,60,70])
print('extended: ',dq)

dq.extendleft([1,2])
print('extendedleft: ',dq)

dq.remove(5)
print('remove success:',dq)

dq.pop()
print('popped: ',dq)

dq.popleft()
print('popped left:',dq)

dq.clear()
print('clear success:',dq)

print('length of queue:',len(dq))

print('count:',dq.count(20))

print('rotate:',dq.rotate(1))

print('reverse: ',dq.reverse())
