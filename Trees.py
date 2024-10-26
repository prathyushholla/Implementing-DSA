"""
Binary Trees

Eg:

           1
       2       3
     4   5   10
"""

class TreeNode:
    def __init__ (self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

    def __str__(self):
        return str(self.val)

# Eg:   
#           1
#       2       3
#     4   5   10

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C 
B.left = D
B.right = E
C.left = F

"""
DFS
Recursive pre-order traversal. Time comlexity: O(n), Space complexity: O(n)
"""

def pre_order(node):
    if not node:
        return 
    
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# pre_order(A)

"""
DFS
In-order traversal
"""

def in_order(node):
    if not node:
        return
    
    in_order(node.left)
    print(node)
    in_order(node.right)

# in_order(A)

"""
DFS
Post-order traversal
"""

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node)

# post_order(A)

"""
DFS 
Iterative pre-order Traversal
"""

def iter_pre_order(node):
    stk = [node]
    
    while stk:
        node = stk.pop()
        print(node)
        if node.right:stk.append(node.right)
        if node.left:stk.append(node.left)

# iter_pre_order(A) 

"""
BFS
Level-order traversal. Time complexity: O(n), Space complexity: O(n)
"""
from collections import deque

def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)

# level_order(A)

"""
DFS
Search for a value. Time complexity: O(n), Space complexity: O(n)
"""

def search(node, target):
    if not node:
        return False

    if node.val == target:
        return True
    
    return search(node.left, target) or search(node.right, target)

# print(search(A, 10))

"""
BSTs
        5
    1       8
  -1  3   7   9 
"""

A2 = TreeNode(5)
B2 = TreeNode(1)
C2 = TreeNode(8)
D2 = TreeNode(-1)
E2 = TreeNode(3)
F2 = TreeNode(7)
G2 = TreeNode(9)

A2.left , A2.right = B2, C2
B2.left , B2.right = D2, E2
C2.left , C2.right = F2, G2 

"""
Search for an element in BST. Time complexity: O(logn), Space complexity: O(logn)
"""

def search_bst(node, target):
    if not node:
        return False
    
    if node.val ==target:
        return True
    
    elif target>= node.val:
        return search_bst(node.right, target)
    
    else:
        return search_bst(node.left, target)
    
print(search_bst(A2,8
                 ))