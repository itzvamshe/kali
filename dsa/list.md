Definition :
     list is a built-in data structure used to store an ordered collection of items     they are dynamic , resizable and capable of storing multiple data types.

    Mutable:list elements can be changed , updated, added or removed after the list    is created.

    Ordered: elements maintain the order in which they are inserted.
    
    Index-based: elements are accessed using their position, starting from index 0.

Data types :

a = 10 | 3.14 | python | True | None | 2+3j | b"Hi"|

10 is integer
3.14 is float
python is str
True | False are bool | boolan
None is None Type
2+3j is complex
b'Hi' is byte

List can be created by :
    
    square brackets | a = [1,2,3]

    constructor | a = list((1,2,3,'apple'))

    repeated elements with (* - multiplication operator) | a[2]*5 

Internal Representation of lists :
    
    Python list stores reference to objects, not the actual values directly

    The list keeps memory address of objects like integers, strings or booleans.

    Actual objects exist separately in memory.

    modifying a mutalbe object inside a list changes the original object.

    reassigning an immutable object creates a new object instead of changingthe old    one.

Accessing elements: By refering to index

EXAMPLE: a = [10,20,30]
        print(a[0]) # first element of any list
        print(a[-1]) # last element of any list

Adding elements to list:

    They are 3 methods to do it

    Append : adds at end of the list.
    
         example: a = [1,2]
                  a.append(3)
                  print(a)

    Insert : adds at a specific position.

         example: a = [1,3]
                  a.insert(1,2)
                  print(a)

    Extend : adds multiple elements to end of the list 

        example: a = [1,2]
                 a.extend([3,4])
                 print(a)

Updating elements in list:

    Since lists are mutable elements can be updated by assigning new values using
    their index.

    Example: a = [10,20,30,40,50]
             a[1] = 25
             print(a)
             [10,25,30,40,50]

Removing elements in list:

    Elements can be removed from a list using 4 methods.

Remove : removes the first occurence of an elements.

    Example: a = [1,2,3]
             a.remove(2)
             print(a) # [1,3]

Pop : removes the element at a specific index | the last element if no index is specified

    Example: a = [1,2,3]
             a.pop()
             print(a) # [1,2]

Del statement: deletes an element of a specified index.

    Example: a = [1,2,3]
             del a[1]
             print(a) # [1,3]

Clear : removes all items.

    Example: a = [1,2,3]
             a.clear()
             print(a) # []

Iterating over lists: 
    
    Lists can be iterated using loops allowing operations to be performed on each element.

    Example: a = ['apple','banana','cherry']
                for item in a :
                    print(item)

Nested lists AKA matrices :

    A nested list is a list that contains another list as its elements. it is commonly used to represent matrices or tabular data.
    Nested elements can be accessed by chaining multiple indexs.

    Example: a = [[1,2],[3,4]]
            print(a[0]) # [1,2]
            print(a[1][0]) # 3
            
