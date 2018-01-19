class Node:
  def __init__(self):
    self.data = None # contains the data
    self.nextNode = None # contains the reference to the next node

# create a linked list without a cycle    
head = Node()
head.data = 0
current = head

for i in range(1,9):
  new_node = Node()
  new_node.data = i
  current.nextNode = new_node
  current = new_node  


def printList(head):
  current = head
  while current.nextNode:
    print current.data
    current = current.nextNode

  print current.data    

def oddsEvens(head):

  temp = None  
  current = head
  head2 = head.nextNode
  count = 1  
  while current.nextNode:
    count += 1    
    temp = current.nextNode
    if temp.nextNode:
      current.nextNode = temp.nextNode
      current = temp
    elif (count % 2 == 0): 
      current.nextNode = head2
      break        
    else:
      current.nextNode = None
      temp.nextNode = head2
      break
        
  printList(head)
  
    
printList(head)    
oddsEvens(head)   
    
  