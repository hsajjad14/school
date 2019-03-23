'''
CSC263 Winter 2019
Problem Set 2, Question 2  Starter Code
University of Toronto Mississauga
'''

# Node for an Augmented Binary Tree with addtional functionality of having a
# count of the number nodes in the tree.
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.count = 1
    
def insert(node, value):
  '''Function that inserts a value into a augmented BST with count attribute.
  '''
  # Always increase the current node count as we are inserting a node in the 
  # subtree.
  node.count += 1
  
  #Case of No Children:
  if node.left == None and node.right == None:
    if node.value >= value:
      node.left = Node(value)
    else:
      node.right = Node(value)
      
  #Case (A) of One Child:
  elif node.left == None and node.right != None:
    if node.value >= value:
      node.left = Node(value)
    else:
      insert(node.right, value)
  
  #Case (B) of One Child:
  elif node.left != None and node.right == None:
    if node.value >= value:
      insert(node.left, value)
    else:
      node.right = Node(value)
  
  #Case of Two Children:  
  else:
    if node.value >= value:
      insert(node.left, value)
    else:
      insert(node.right, value)

def num_orders(lst):
  # In the case the list is only 0 or 1 elements we can quickly return 1.
  # This allows us to assume a list of at least 2 elements for the remainder
  # of our function.
  if len(lst) <= 1:
    return 1
  
  bst = Node(lst[0])
  i = 1
  while i < len(lst):
    insert(bst, lst[i])
    i += 1
    
  return int(num_orders_helper(bst))
  

def num_orders_helper(bst):
  if bst == None:
    return 1
  else:
    
    #Cases to handle if there is no left or right child:
    if bst.left != None:
      total_left = bst.left.count
    else:
      total_left = 0
      
    if bst.right != None:
      total_right = bst.right.count
    else:
      total_right = 0
    
      
    total_children = total_left + total_right
    
    # Now we build our multiplier which represents the number of permutations
    # where we have two sequences that can be interwoven together.
    total_children_factorial = fact(total_children)
    total_left_factorial = fact(total_left)
    total_right_factorial = fact(total_right)   
    multiplier = total_children_factorial / (total_left_factorial * total_right_factorial)
    
    return multiplier * num_orders_helper(bst.left) * num_orders_helper(bst.right)
  
  
  
def fact(n):
  '''Function that returns n!
  '''
  if n == 0:
    return 1
  else:
    return n * fact(n - 1)
  
if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert 2 == num_orders([2, 1, 3])
  # Case 2
  assert 8 == num_orders([4, 2, 1, 5, 3])
