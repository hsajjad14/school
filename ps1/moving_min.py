'''
CSC263 Winter 2019
Problem Set 1 Starter Code
University of Toronto Mississauga
'''

# Do NOT add any "import" statements
class Node:
    """A node in a binary tree."""

    def __init__(self, item: object, parent=None, left=None, right=None) -> None:
        """Initialize this node.
        """
        self.item,self.parent ,self.left, self.right =  item, parent, left, right
        
    
class Heap:
    
    def __init__(self) -> None:
        self.heap_ls = []
        self.size = 0
    
    def insert(self,n: int):
        self.size+=1
        self.heap_ls.append(n)
        self.bubble_up(self.size)
        
    def bubble_up(self,i:int):
        #print(i)
        #print(self.size//2)
        while i//2>0:            
            if self.heap_ls[i-1] < self.heap_ls[(i-1)//2]:
                temp = self.heap_ls[i-1]
                self.heap_ls[i-1] = self.heap_ls[(i-1)//2]
                self.heap_ls[(i-1)//2] = temp
            i=i//2
        
def solve_moving_min(commands):
    '''
    Pre: commands is a list of commands
    Post: return list of get_min results
    '''
    # TODO: implement this function
    h = Heap()
    ret_list=[]
    count_min = 0
    for i in commands:
        stuff = i.split()
        if len(stuff) == 2:
            if stuff[1][0] == '-':
                h.insert(-(int)(stuff[1][1:]))                
            else:
                h.insert((int)(stuff[1]))
        elif(stuff[0]=="get_min"):
            count_min+=1            
            ret_list.append(get_min(count_min,h.heap_ls))
    return ret_list


#def min_at(i:int,heap_ls):
    
    #copy = heap_ls[:]
    
    #while i > 0:
        #left = copy[0]
        #right = copy[1]
        
        #if left < right:
            #copy.pop(0)
        #else:
            #copy.pop(1)
        
        #print(copy)
        #i -=1
    
    #if copy!=[]:
        #left = copy[0]
        #if len(copy) >= 2:
            #right = copy[1]
        #else:
            #right = copy[0]
    
    #if left < right:
        #return left
    #else:
        #return right
    
    
    

def get_min(i:int,heap_ls):
    count = 0
    #if i ==0:
     #   return heap_ls[0]
    
    if i == 1:
        return heap_ls[0]
    
    f=True
    
    while f:

        if i > 2**(count+1)-1:
            count += 1            
        else:
            f = False         
    
        if count == len(heap_ls)-1:
            f = False         


    mins = []
    #min2 = heap_ls[len(heap_ls)-1]
    #min1 = heap_ls[len(heap_ls)-1]
    mins = []
    
    copy =[] 
    #print(count)
    if 2**(count+1)-1 > len(heap_ls):
        copy = heap_ls[2**count-1:]
        copy.sort()
        #print(i,i-(2**(count-1+1)-1) - 1)
        #print(i-(len(heap_ls)-1)-1)        
        #print(copy)
        return copy[i-(2**(count-1+1)-1) - 1]
            
        
    else:
        
        copy = heap_ls[2**count-1:2**(count+1)-1]
        copy.sort()
        #print(count)
        #print(i,2**(count-1+1)-1)
        #print(i-(2**(count-1+1)-1) - 1)
        return copy[i-(2**(count-1+1)-1) - 1]

            
        
            

if __name__ == '__main__':
    
    assert [10, 5, 10] == solve_moving_min(
   ['insert 10',
    'get_min',
    'insert 5',
    'insert 2',
    'insert 50',
    'get_min',
    'get_min',
    'insert -5'
   ])