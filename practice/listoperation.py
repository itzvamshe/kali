a = [1,2,3,4,5]
print(a,'default list')

# append

a.append(6)
print(a,'append new value')

# extend
a.extend([7,8,9,10])
print(a,'extend new values')

# repeated multipler
b=[1]*5
print(b,'list multiplied by 5')
c=[2]*5
print(c,'list mulitplied by 5')

# insert 
b.insert(3,50)
print(b,'inserted 50')

# update
b[3] = 1
print(b,'updated 50 to 1 again')


# remove selection remove,pop,clear,del

# remove
c.remove(2)
print(c,'it only removes the first occurance of 2 so no of values are 4.')

# pop
c.pop()
print(c,'its poped last element so no of values are 3.')

# del
del c[0]
print(c,'it deleted the first element using del.')

# clear
c.clear()
print(c,'it cleared the list - c.')

# for iterating adding elements in c.
c.extend(['apple','mango','banana'])
print(c,'extended again.')

#iterating

for i in c:
    print(i)

print('iteration succes')


# nested lists

# | 1,2 |
# | 3,4 |


x = [[1,2],[3,4]]

print(x)

print('indexs')
print(x[0][0])
print(x[0][1])
print(x[1][0])
print(x[1][1])
print('success')
