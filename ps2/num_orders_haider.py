'''
CSC263 Winter 2019
Problem Set 2, Question 2  Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements

def num_orders(lst):
  
  if lst == []:
    return 1

  l = num_left_children(lst)
  r = num_right_children(lst)
  
 # print(left_children(lst), right_children(lst))
  return int(intercombinations(l,r)*num_orders(left_children(lst))*num_orders(right_children(lst)))

def left_children(lst):
  l = []
  root = lst[0]
  for x in range(len(lst)):
    if x != 0 and lst[x] <= root:
      l.append(lst[x])
  
  return l
      
def right_children(lst):
  l = []
  root = lst[0]
  for x in range(len(lst)):
    if x != 0 and lst[x] > root:
      l.append(lst[x])  
  
  return l
  
def num_left_children(lst):
  
  root = lst[0]
  num = 0
  for i in range(len(lst)):
    if i != 0 and root >= lst[i]:
      num +=1

 #print(num,"aAAAAAAAAA")
  return num

def num_right_children(lst):
  
  root = lst[0]
  num = 0
  for i in range(len(lst)):
    if i != 0 and root < lst[i]:
      num +=1
  
  return num

def intercombinations(l:int,r:int):
  
  #nCr = n!/r!(n-r)

  n = l+r
  
  n_f = permutation(n)
  

  l_f = permutation(l)
  nl_f = permutation(n-l)  
  return (n_f/(l_f*nl_f))

def permutation(n):
  
  mult = 1
  for i in range(1,n+1):
    mult = i*mult
  
  return mult
  
  

if __name__ == '__main__':
  pass
  # some small test cases
  # Case 1
  #assert 2 == num_orders([2, 1, 3])
  # Case 2
  #assert 8 == num_orders([4, 2, 1, 5, 3])