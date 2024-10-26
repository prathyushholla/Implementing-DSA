"""
Stacks 
"""

"""
Adding elements to stacks. In a list you access only the rightmost element of the list.
"""
s =[]
s.append(5)
s.append(6)
s.append(7)
s.append(8)
s.append(9)

# print(s)

"""
remove an element 
"""
x = s.pop()
# print(x)
# print(s)
"""
peek
""" 
# print(s[-1])

"""
Queues 
"""

"""
Enqueue. Using lists you enqueue from one end.
"""

q = []
q.insert(0,4)
q.insert(0,5)
q.insert(0,6)
print(q)

"""
Dequeue. Using lists you dequeue from the other end.
"""
x = q.pop()
# print(q)

"""
Peek. Take a look first element. 
"""
print(q[-1])