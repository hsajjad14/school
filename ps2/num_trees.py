'''
CSC263 Winter 2019
Problem Set 2, Question 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.height = 1
    self.balance_factor = 0
    self.num_leaves = 1
    self.is_leaf = True
    self.count = 1
  
    
class List:
  def __init__(self):
    self._data = []
    
  def add(self, data):
    self._data.append(data)
    
  def get(self, i):
    return self._data[i]
    
def insert(node, value):
  node.count += 1
  node.is_leaf = False
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
    
  # Now we call our helper functions to set the height and balance factor
  # of the node
  set_height(node)
  set_balance_factor(node)
  set_leaf_count(node)
  


def set_height(bt):
  if bt.left and bt.right:
    bt.height = max(bt.left.height, bt.right.height) + 1
  elif bt.left:
    bt.height = bt.left.height + 1
  elif bt.right:
    bt.height = bt.right.height + 1
  else:
    pass
  
  
def set_balance_factor(bt):
  if bt.left and bt.right:
    bt.balance_factor = bt.right.height - bt.left.height
  elif bt.left:
    bt.balance_factor = 0 - bt.left.height
  elif bt.right:
    bt.balance_factor = bt.right.height - 0
  else:
    pass
    
def perm_generator(n, current_perm, all_perms):
  '''returns a array of each of the permutations from 1 to n using Heap's
     Algorithm.
  '''
  if n == 1:
    all_perms.add(current_perm[:])
  else:
    i = 0
    while i < (n - 1):
      perm_generator(n - 1, current_perm, all_perms)
      if n % 2 == 0:
        current_perm[i], current_perm[n-1] = current_perm[n-1], current_perm[i]
      else:
        current_perm[0], current_perm[n-1] = current_perm[n-1], current_perm[0]
        
      i += 1
    perm_generator(n-1, current_perm, all_perms)
     
      
  
def get_perms(n):
  i = 1
  array = []
  while i <= n:
    array.append(i)
    i += 1
  perms = List()
  perm_generator(n, array, perms)
  perm_as_list = []
  j = 0
  while (j < fact(n)):
    perm_as_list.append(perms.get(j))
    j += 1
  return perm_as_list
    
    
  
  
def set_leaf_count(bt):
  if bt.left and bt.right:
    bt.num_leaves = bt.left.num_leaves + bt.right.num_leaves
  elif bt.left:
    bt.num_leaves = bt.left.num_leaves
  elif bt.right:
    bt.num_leaves = bt.right.num_leaves
  else:
    bt.num_leaves = 1
    
def fact(n):
  '''Function that returns n!
  '''
  if n == 0:
    return 1
  else:
    return n * fact(n - 1)    

def num_trees(nodes, leaves):
  if nodes <= 0:
    return 1
  else:
    num_trees = 0
    trees = []
    perms = get_perms(nodes)
    for perm in perms:
      bt = Node(perm[0])
      i = 1
      while i < len(perm):
        insert(bt, perm[i])
        i += 1
      if ( (bt.num_leaves == leaves) and check_balance_factor(bt) ):
        not_duplicate = True
        for tree in trees:
          if duplicate_trees(tree, bt):
            not_duplicate = False
            
        if not_duplicate:
          trees.append(bt)
    
    return len(trees)
        
      
def duplicate_trees(t1, t2):
  if not(t1) or not(t2):
    if not(t1) and not(t2):
      return True
    else:
      return False
  else:
    # Both nodes, are leaves
    if t1.is_leaf and t2.is_leaf:
      return True
    # Both nodes have 2 children
    elif t1.left and t1.right and t2.left and t2.right:
      return duplicate_trees(t1.left, t2.left) and duplicate_trees(t1.right, t2.right)
    
    elif (t1.left and t2.left) and (t1.right == None and t2.right == None):
      return duplicate_trees(t1.left, t2.left)
    
    elif (t1.left == None and t2.left == None) and (t1.right and t2.right):
      return duplicate_trees(t1.right, t2.right)
    else:
      return False
    
      
    
def check_balance_factor(node):
  if node.is_leaf:
    return (-1 <= node.balance_factor <= 1)
  elif node.left and node.right:
    return ( (-1 <= node.balance_factor <= 1) and check_balance_factor(node.left) and check_balance_factor(node.right))
  elif node.left:
    return ( (-1 <= node.balance_factor <= 1) and check_balance_factor(node.left) )
  elif node.right:
    return ( (-1 <= node.balance_factor <= 1) and check_balance_factor(node.right) )
            
if __name__ == '__main__':

  # some small test cases
  # Case 1
  assert 2 == num_trees(5, 3)