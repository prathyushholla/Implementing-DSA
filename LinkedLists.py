# Linked Lists 

# Singly Linked lists 

class SinglyNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next 
    
    def __str__(self):
        return str(self.data)
    

# Head = SinglyNode(7, A)
# A = SinglyNode(8, B)
# B = SinglyNode(9, C)
# C = SinglyNode(10, D)
# D = SinglyNode(22)
# E = SinglyNode(40)
# F = SinglyNode(60)

# Head.next = A
# A.next = B
# B.next = C
# C.next = D
# D.next = E
# E.next = F

#printing all elements    
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

# display(Head)

# Searching for elements 
def search(head, val):
    curr = head 
    while curr:
        if curr.val == val:
            return True
        curr = curr.next 
    
    return False

# print(search(Head, 41))

# Doubly Linked Lists 

class DoublyNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.val)
    
Dhead = DoublyNode(1)
A = DoublyNode(2)
B = DoublyNode(3)
C = DoublyNode(4)

Dhead.next = A
A.next = B
A.prev = Dhead
B.next = C
B.prev = A
C.prev = B

curr = C 

while curr:
    print(curr.val)
    curr = curr.prev



