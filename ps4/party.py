'''
CSC263 Winter 2019
Problem Set 4 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
class vertex:
  
  def __init__(self, x):
    self.name = x
    self.neighbours = []
    
    self.d = 0
    self.f = 0
    self.colour = 'white'
  
  def add_neighbour(self, v):
    #neighbour_set = set(self.neighbours)
    print("hmm??"+str(self.neighbours))
    if v not in self.neighbours:
      self.neighbours.append(v)
      self.neighbours.sort(key=lambda x:x.name, reverse=False)
      
  def __str__(self):
    for x in self.neighbours:
      print(x.name)
  
  
class graph:
  def __init__(self):
    self.vertices = {}
    self.time = 0
    self.l= []
  
  def add_vertex(self,v):
    if isinstance(v, vertex) and v.name not in self.vertices:
      self.vertices[v.name] = v
      #temp = {}
      
      #for key in sorted(self.vertices):
        #temp[key] = self.vertices[key]
      
      #self.vertices = temp
      
      return True
    else:
      return False
  
  def add_edge(self, x, y):
    
    if x.name in self.vertices and y.name in self.vertices:
      for k,v in self.vertices.items():
        if k == x.name:
          v.add_neighbour(y)
        if k == y.name:
          v.add_neighbour(x)
          
      return True
    
    else:
      return False
    
  def print_g(self):
    for k,v in self.vertices.items():
      print(k+ ": ")
      for j in v.neighbours:
        print("    "+j.name)
  
  l  = []
  def dfs_help(self, v):
    global time
    v.colour = 'gray'
    v.d = time
    time+=1
    global l
    self.l.append(v.name)
    
    print(v.name)
    
    for x in v.neighbours:
      if self.vertices[x.name].colour == 'white':
        self.dfs_help(self.vertices[x.name]);
    
    v.colour = 'black'
    v.f = time
    time += 1
    
    return self.l
    
  def dfs(self,v):
    global time
    time = 1
    s = []
    s = self.dfs_help(v)
   # print(s)
    for k,v in self.vertices.items():
      v.d = 0
      v.f = 0
      v.colour = 'white'      
    
    self.l = []
    return s
    
      
  
  

def solve_party(commands):
  '''
  Pre: commands is a list of commands
  Post: return list of 'tell' results
  '''
  l = []
  graph_students = graph()
  ret = []
  com = ''
  for stuf in commands:
    l = stuf.split()
   # print(l)
    if l[0] == 'tell':
      if l[2] in graph_students.vertices and l[1] in graph_students.vertices:
        if l[1] in graph_students.dfs(graph_students.vertices[l[2]]) or l[2] in graph_students.dfs(graph_students.vertices[l[1]]):
          c1 = check_distance(l, graph_students,1)
          c2 = check_distance(l, graph_students,2)
          
          if c1 < c2:
            if c1 % 2 == 0:
              com = 'same'
            else:
              com = 'different'
              
          elif c1 > c2:
            if c2 % 2 == 0:
              com = 'same'
            else:
              com = 'different'
          elif c1 == c2:
            if c2 % 2 == 0:
              com = 'same'
            else:
              com = 'different'
        else:
          com = 'unknown'          
      else:
        com = 'unknown'
          
      ret.append(com)
      
      
    elif l[0] == 'add':
      s1 = vertex(l[1])
      s2 = vertex(l[2])
      graph_students.add_vertex(s1)
      graph_students.add_vertex(s2)
      graph_students.add_edge(s1, s2)
      
  return ret

def check_distance(l,graph_students,num):
  dfs_ret = []
  dfs_ret = graph_students.dfs(graph_students.vertices[l[num]])
  count = 0
  flag = False
  for n in dfs_ret:
    
    if num == 1:
      if n == l[2]:
        flag = True
       # count += 1   
        
      
      if n != l[2] and flag == False:
        count += 1   
    else:
      if n == l[1]:
        flag = True
        #count += 1   
        
      
      if n != l[1] and flag == False:
        count += 1       
  
  return count
      
  

if __name__ == '__main__':
 # pass
  #pass
  # some small test cases
  # Case 1
  assert ['unknown', 'different', 'same'] == solve_party(
    ['tell 1 3',
     'add 1 3',
     'tell 1 3',
     'add 3 4',
     'tell 1 4'
    ])
  
  assert ['unknown','different','different','different','same','different','different'] == solve_party(
      ['tell a b',
       'add a b',
       'tell a b',
       'add b d',
       'tell b d',              
       'add d c',
       'tell d c',
       'tell b c',
       'tell b d',
       'tell a c'            
      ])
  
