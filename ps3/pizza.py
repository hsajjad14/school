'''
CSC263 Winter 2019
Problem Set 3 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
# Do NOT use Python dictionaries
def hash_func(input_list):
  '''Simple hash of adding elements of a list together
  '''
  total = 0
  for item in input_list:
    total += item
    
  return total

def num_pizza_kinds(pizzas):
  '''
  Pre: pizzas is a list of pizza 5-tuples
  Post: return number of kinds of pizzas
  '''
  total_unique = 0
  i = 0
  unique_pizzas = []
  while i < len(pizzas):
    unique_pizzas.append(None)
    i += 1
    
  for pizza in pizzas:
    index = hash_func(pizza) % len(pizzas)
    if not unique_pizzas[index]:
      unique_pizzas[index] = [pizza]
      total_unique += 1
    
    else:
      if unique(pizza, unique_pizzas[index]):
        unique_pizzas[index].append(pizza)
        total_unique += 1
        
  return total_unique
      
      
def unique(pizza1, pizza_list):
  for pizza in pizza_list:
    pizza_2_concat = pizza + pizza
    offset = 0
    while offset < 7:
      pizza_to_compare = pizza_2_concat[offset: offset + 5]
      if pizza1 == pizza_to_compare:
        return False
      offset += 1
  return True

if __name__ == '__main__':

  # some small test cases
  # Case 1
  pizzas = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 1), (5, 4, 3, 2, 1), (4, 3, 2, 1, 5), (20, 10, 2, 9, 1)]
  assert 3 == num_pizza_kinds(pizzas)