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
    #print("hmm??"+str(self.neighbours))
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
      print(k+ ": diistance is"+ str(v.d) )
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
    
    #print(v.name)
    
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
  
  def bfs_dist(self, initial):
    queue = []
    self.vertices[initial].d = 0
    self.vertices[initial].colour = 'gray'
    
    queue.append(self.vertices[initial])
    #for j in self.vertices[initial].neighbours:
      #j.d = self.vertices[initial].d + 1
      #queue.append(j)
    
    while len(queue) > 0:
      node = queue.pop(0)
      node.colour = 'gray'
      
      for k in node.neighbours:
        if k.colour =='white':
          queue.append(k)
          #if k.d > node.d + 1:
          k.d = node.d + 1
          print(k.name + " dist " + str(k.d))
          
            
      
  def bfs(self,begining, end):
    queue = []
    self.vertices[begining].d = 0
    self.vertices[begining].colour = 'gray'

    if begining == end:
      return [[begining]]
    
    queue.append(self.vertices[begining].neighbours)
    
    while queue != []:
      
          
      path = queue.pop(0)

      #print path
      tp = []
      for x in path:
        tp.append(x.name)
        
      print(tp)
      last = path[-1]
      #print(last.name)

      
      for next_to in last.neighbours:
        print(next_to.name)
        if next_to.colour == 'white':
          new_p = list(path)
          new_p.append(next_to)
          queue.append(new_p)
          if next_to.name == end:
            tp = []
            for x in new_p:
              tp.append(x.name)               
            return new_p
          
          if next_to.d > last.d + 1:
            next_to.d  = last.d + 1           
      
      
      
      
      
      
  
  

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
          graph_students.bfs_dist(l[1])
          if graph_students.vertices[l[2]].d % 2 == 0 and graph_students.vertices[l[2]].d != 0:
            com = 'same'
          else:
            com = 'different'
        else:
          com = 'unknown'  
          
      else:
        com = 'unknown'
      
      
      for keys, values in graph_students.vertices.items():
        values.d = 0      
        values.colour = 'white'
      ret.append(com)
      
      
    elif l[0] == 'add':
      if l[1] not in graph_students.vertices:
        s1 = vertex(l[1])
        graph_students.add_vertex(s1)
        
      if l[2] not in graph_students.vertices:
        s2 = vertex(l[2])
        graph_students.add_vertex(s2)
      graph_students.add_edge(graph_students.vertices[l[1]],graph_students.vertices[l[2]])
      
  return ret

def check(l,g):
  for x in l:
    k = x.split()
    if(k[0] == 'add'):
      if k[1] not in g.vertices:
        s1 = vertex(k[1])
        g.add_vertex(s1)
        
      if k[2] not in g.vertices:
        s2 = vertex(k[2])
        g.add_vertex(s2)
        
        
      g.add_edge(g.vertices[k[1]],g.vertices[k[2]])
    else:
      pass    
      #bfs_ret = g.bfs(l[1],l[2])
      #c1 = len(bfs_ret)
      #if c1 % 2 == 0:
        #com = 'same'
      #else:
        #com = 'different'      
    

  
  

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
  
