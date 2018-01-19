import random
# max operation on a stack

class Node:
  def __init__(self):
    self.data = None # contains the data

class StackNode:
  def __init__(self):
    self.maxNode = None # contains the data  
    self.nextNode = None

class Stack:
  def __init__(self):
    self.head = None      
        
  def push(self, node):
     
    toAdd = StackNode()       
    if self.head:
      toAdd.nextNode = self.head
      if node.data > self.head.maxNode.data:
        toAdd.maxNode = node
      else:
        toAdd.maxNode = self.head.maxNode               
    else:
      toAdd.maxNode = node
    self.head = toAdd  
        
       
  def pop(self):
    toReturn = None  
    if self.head:
      toReturn = self.head
      if self.head.nextNode:
        self.head = self.head.nextNode
      else:
        self.head = None
        
    return toReturn  
      
  def max(self):
   return self.head.maxNode.data 
    
    
    
stack = Stack()
for i in range (0,10):
  node = Node()
  node.data = random.randint(1,20)
  print "Pushing: " + str(node.data)
  stack.push(node)

print stack.max()    