
# coding: utf-8

# In[ ]:


from collections import defaultdict,deque 

class BipGraph(): 
    
    def __init__(self, V): 
        self.V = V 
        self.gr = [[0 for column in range(V)] for row in range(V)]
        
    def Check_if_Bipartite(self, p): 
        cArr = [-1] * self.V 
        cArr[p] = 1
        queue = [] 
        queue.append(p) 
        while queue: 
            u = queue.pop() 
            if self.gr[u][u] == 1: 
                return False; 
            for v in range(self.V): 
                if self.gr[u][v] == 1 and cArr[v] == -1: 
                    cArr[v] = 1 - cArr[u] 
                    queue.append(v) 
                elif self.gr[u][v] == 1 and cArr[v] == cArr[u]: 
                    return False
        return True
    
class Dij_Class(object):
    
    def __init__(self):
        self.nodes = set()
        self.edg = defaultdict(list)
        self.lengths = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        
    def add_edge(self, from_node, to_node, length):
        self.edg[from_node].append(to_node)
        self.edg[to_node].append(from_node)
        self.lengths[(from_node, to_node)] = length
        self.lengths[(to_node, from_node)] = length 
        
        
    def BreadthFirstSearch(self, s): 
        visited = {}
        for i in self.edg:
            visited[i] = False
        queue = [] 
        queue.append(s)
        visited[s] = True
        while queue: 
            s = queue.pop(0) 
            print (s, end = " ") 
            for i in self.edg[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True  
                    
                    
    def DepthFirstSearchU(self,v,visited): 
        visited[v]= True
        print (v,) 
        for i in self.edg[v]: 
            if visited[i] == False: 
                self.DepthFirstSearchU(i, visited) 
                
                
    def DepthFirstSearch(self,v):
        visited = {}
        for i in self.edg:
            visited[i] = False
        self.DepthFirstSearchU(v,visited)
               
class Cycle(): 
    
    def __init__(self,vertices): 
        self.gr = defaultdict(list) 
        self.V = vertices 
    
    def add_edge(self,u,v): 
        self.gr[u].append(v) 
              
    def CheckCycU(self, v, visited, rec): 
        visited[v] = True
        rec[v] = True
        for neighbour in self.gr[v]: 
            if visited[neighbour] == False: 
                if self.CheckCycU(neighbour, visited, rec) == True: 
                    return True
            elif rec[neighbour] == True: 
                return True
        rec[v] = False
        return False       
    
    def CheckCyc(self): 
        visited = [False] * self.V 
        rec = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.CheckCycU(node,visited,rec) == True: 
                    return True
        return False
    
    
    def CheckCycU2(self, v, visited, par): 
        visited[v] = True
        for i in self.gr[v]: 
            if visited[i] == False: 
                if self.CheckCycU(i, visited, v) == True: 
                    return True
            elif i != par: 
                return True
        return False 
    
    
    def Check_if_Tree(self): 
        visited = [False] * self.V 
        if self.CheckCycU2(0, visited, -1) == True: 
            return False
        for i in range(self.V): 
            if visited[i] == False: 
                return False
        return True
        
def i_b(edg,tv1,tv2): 
    edg = []
    print(tv1)
    print(tv2)
    for i in range(0,edg):
        if tv1[i].isdigit() and tv2[i].isdigit():
            v = [int(tv1[i]),int(tv2[i])]
            edg.append(v)
        else:
            tv1[i] = ord(tv1[i])-96
            tv2[i] = ord(tv2[i])-96
            v = [tv1[i],tv2[i]]
            edg.append(v)

    return edg   
    
def dj(gr, initial):
    visited = {initial: 0}
    path = {}
    nodes = set(gr.nodes)
    while nodes:
        minnode = None
        for node in nodes:
            if node in visited:
                if minnode is None:
                    minnode = node
                elif visited[node] < visited[minnode]:
                    minnode = node
        if minnode is None:
            break
        nodes.remove(minnode)
        current_weight = visited[minnode]
        for edge in gr.edg[minnode]:
            try:
                weight = current_weight + gr.lengths[(minnode, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = minnode
    return visited, path


def SP(gr, org, dest):
    visited, paths = dj(gr, org)
    fpath = deque()
    _dest = paths[dest]
    while _dest != org:
        fpath.appendleft(_dest)
        _dest = paths[_dest]
    fpath.appendleft(org)
    fpath.append(dest)
    return visited[dest], list(fpath)

def ini(ed,tv1,tv2): 
    edgss = []
    for i in range(0,ed):
        if tv1[i].isdigit() and tv2[i].isdigit():
            g.add_edge(int(tv1[i]), int(tv2[i]))
            v = [int(tv1[i]),int(tv2[i])]
            edgss.append(v)
        else:
            tv1[i] = ord(tv1[i])-96
            tv2[i] = ord(tv2[i])-96
            g.add_edge(int(tv1[i]), int(tv2[i]))
            v = [int(tv1[i]),int(tv2[i])]
            edgss.append(v)
    return edgss



Choices = {}
print('--------------------------------------------Menu----------------------------------------------------')
Choices['1.']="Create a Directed Graph" 
Choices['2.']="Perform BreadthFirstSearch Traversal on the Graph"
Choices['3.']="Perform DFS Traversal on the Graph."
Choices['4.']="Find Shortest Path from Source to all vertices using dj’s shortest path Algorithm"
Choices['5.']="Detect if there is a Cycle in the graph."
Choices['6.']="Check if the graph is Bipartite or not."
Choices['7.']="Check if Graph is a tree or not."
Choices['8.']="Exit"
gr = Dij_Class()
g = Cycle(10)
g1 = BipGraph(4)
nodes = []
edgss = []
e2 = []
v1 = []
v2 = []
w = []
while True: 
    opts=Choices.keys()
    sorted(opts)
    print('\n')
    for e in opts: 
        print (e, Choices[e])
    choice=input("Please Select:") 
     
    if choice =='1': 
        while True:
            vert = input('Please Enter the number of Vertices:')
            if vert is None:
                raise TypeError
            elif vert.isalnum() == False:
                print('False input')
            elif vert == '':
                print('No input')
            else:
                vert = int(vert)
                for i in range(0,vert):
                    val = input('Enter the Vertex value :')
                    nodes.append(val)

                for node in nodes:
                    gr.add_node(node)
                edg = int(input('enter the number of edges: '))
                for i in range(0,edg):
                    ver1 = input('Enter (from) Vertex:')
                    ver2 = input('Enter (To) Vertex:')
                    wei = int(input('Please enter weight'))
                    e = [ver1,ver2]
                    edgss.append(e)
                    v1.append(ver1)
                    v2.append(ver2)
                    w.append(wei)
                for i in range(0,edg):
                    gr.add_edge(v1[i], v2[i], w[i])
                c1 = v1
                c2 = v2
                b1 = v1
                b2 = v2
                t1 = v1
                t2 = v2
                break
            print('Graph ->' + nodes)
                  
    elif choice == '2':
        print('\n')
        while True:
            p = input('Enter source node : ')
            if p is None:
                raise TypeError
            elif p.isalnum() == False:
                print('Incorrect input, sorry')
            elif p == '':
                print('No entry')
            elif p not in nodes:
                print('No vertex, try again')
            else:
                gr.BreadthFirstSearch(p)
                break
                           
    elif choice == '3':
        print('\n')
        while True:
            p = input('Enter the source node')
            if p is None:
                raise TypeError
            elif p.isalnum() == False:
                print('wrong input')
            elif p == '':
                print('No value entered')
            elif p not in nodes:
                print('No vertex is present, enter again')
            else:
                gr.DepthFirstSearch(p)
                break
                
                           
    elif choice == '4': 
        print('\n')
        while True:
            print('Enter starting node')
            p = input()
            if p is None:
                raise TypeError
            elif p.isalnum() == False:
                print('wrong input')
            elif p == '':
                print('You did not enter a value')
            elif p not in nodes:
                print('The Vertex is not Present! Enter again')
            else:
                if len(nodes) < 2:
                    print('edge is between {} & Cost is : {}'.format(edgss,w))
                    break
                else:
                    for i in nodes:
                        if p != i:
                            print('Path: {} -> {}'.format(p,i))
                            print(SP(gr, p, i)) 
                    break
                    
                               
    elif choice == '5': 
        print('\n')
        if len(e2)<1:
            e2 = ini(edg,c1,c2)
            if g.CheckCyc() == 1: 
                print ("The Graph has a cycle")
            else: 
                print ("The Graph has no cycle")
        else:
            if g.CheckCyc() == 1: 
                print ("The Graph has a cycle")
            else: 
                print ("The Graph has no cycle")
                
                            
    elif choice == '6': 
        print('\n')
        if len(e2)<1:
            e2 = ini(edgss,b1,b2)
            max = len(e2) + len(e2)
            m = [[0 for x in range(0,max)]for x in range(0,max)]
            for i in e2:
                a = i[0]-1
                b = i[1]-1
                m[a][b] = 1
            g1.gr = m
            print ("the graph is Bipartite" if g1.Check_if_Bipartite(0) else "the graph isn't bipartite")
        else:
            max = len(e2) + len(e2)
            m = [[0 for x in range(0,max)]for x in range(0,max)]
            
            for i in e2:
                a = i[0]-1
                b = i[1]-1
                m[a][b] = 1
            g1.gr = m
            print ("the graph is Bipartite" if g1.Check_if_Bipartite(0) else "the graph isn't bipartite")
            
                  
    elif choice == '7':
        print('\n')
        if len(e2)<1:
            e2 = ini(edg,t1,t2)
            if g.Check_if_Tree()==True:
                print('Yes, the graph is a tree')
            else:
                print('No, the graph is not tree')
            print('\n')
        else:
            if g.Check_if_Tree()==True:
                print('Yes, the graph is a tree')
            else:
                print('No, the graph is not tree')
            print('\n')
                   
    elif choice == '8': 
        print('Done')
        break
        
    else: 
        print ("Incorrect choice")


# In[ ]:


a

