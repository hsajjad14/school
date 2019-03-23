'''
CSC263 Winter 2019
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries

def num_pizza_kinds(pizzas):
  '''
  Pre: pizzas is a list of pizza 5-tuples
  Post: return number of kinds of pizzas
  '''
  pizzas_d = []
  num = 0
  for pizza in pizzas:
    p = shift(pizza)
    #print(p)
    if tuple(p) not in pizzas_d:
      pizzas_d.append(tuple(p))
      num+=1
  
  print(pizzas_d)
  return len(pizzas_d)

def sort_pizza(tup_pizza):
  
  return sorted(tup_pizza)


def shift(t):
  i = 0
  s = list(t)
  #z=s[:]
  for x in s:
    
    if min(s) == x:
    #if i == 0:
     # return s
    #else:
      #print(i)
      if(duplicates(s,i) == False):
        r = i-1
        z = s[:]
        c = 0
        for l in s:
          r+=1          
          z[c] = s[r%len(s)]
          c+=1 
        break
      else:
        p = False
        for j in range(len(s)):
          if max(s) == s[j]:
            #if(duplicates(s,j) == False):
            r = j-1
            z = s[:]
            c = 0
            for l in s:
              r+=1          
              z[c] = s[r%len(s)]
              c+=1
            p = True
            break              
            
        if p == True:
          break

    if i == len(s) - 1:
      i = 0
    else:
      i+=1
    
  return z
    
def duplicates(z,i):
  r=i
  c=0
  s=z[:-1]
  for j in range(1,5):
    r+=1
    s[c]= z[r%len(z)]
    c+=1
  
  #print(s)
  return z[i] in s
      
    
  
if __name__ == '__main__':

  # some small test cases
  # Case 1
  pizzas = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 1), (5, 4, 3, 2, 1), (4, 3, 2, 1, 5), (20, 10, 2, 9, 1)]
  #assert 3 == num_pizza_kinds(pizzas)