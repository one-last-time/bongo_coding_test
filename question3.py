tree = []
vis = []
level = []
sparse_table = []
nodes=[]

#initialize the lists
for i in range(500000):
    tree.append([])
    vis.append(0)
    level.append(0)
    sparse_table.append([])
    for j in range(12):
        sparse_table[i].append(-1)


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent




def Get_imidiate_parents(id):
    
    '''
    find the imidiate parent or 0 level parent of each node in the tree
    find level of each node in tree 
    '''
    vis[id]=1
    for i in tree[id]:
        if vis[i]==0:
            vis[i] = 1
            sparse_table[i][0]=id
            level[i] = level[id]+1
            Get_imidiate_parents(i)

def Get_all_level_parents(root,node_count=0):
    '''
    populate the sparse table to find 0 to logn level parents of each node

    '''
    #get all zero level parents
    Get_imidiate_parents(root)
    
    for i in range(1,12):
        for j in range(node_count):
            p=sparse_table[j][i-1]
            if p!=-1:
                sparse_table[j][i] = sparse_table[p][i-1]
            

def LCA(a,b):
    '''
    find LCA of the two given nodes
    '''
    if level[a] < level[b]:
        a, b = b, a
    
    #pull both node to the same level
    for i in range(11,-1,-1):
        if level[a]-(1<<i) >= level[b]:
            a=sparse_table[a][i]
    if a==b:
        return a
    
    for i in range(11,-1,-1):
        if sparse_table[a][i]!=-1 and sparse_table[b][i]!=-1 and sparse_table[a][i]!=sparse_table[b][i]:
            a=sparse_table[a][i]
            b=sparse_table[b][i]
    return sparse_table[a][0]


def build_graph_and_query(node_tuples,querie_tuples):
    '''
    node_tuples is a list of tuple(value,parent) of the given graph
    quires is list of tuples(node1,node2) to get LCA for.
    Returns a list of answer for the queries
    '''
    #build graph from given nodes
    for item in node_tuples:
        nodes.append(Node(item[0],item[1]))
    #find root and build graph
    root = -1

    for item in nodes:
        if item.parent!=None:
            tree[item.parent].append(item.value)
            tree[item.value].append(item.parent)
        else:
            root = item.value

    #Populate the sparse table for given tree
    Get_all_level_parents(root,len(nodes)+1)
    ans=[]
    for item in querie_tuples:
        ans.append(LCA(item[0],item[1]))
    return ans



#get nodes

nd =[(1,None),(2,1),(3,1),(4,2),(5,2),(6,3),(7,3),(8,4),(9,4)]
qs=[(9,5),(1,9),(1,7),(4,9),(9,7),(1,1)]

print(build_graph_and_query(nd,qs))

'''
nodes.append(Node(1,None))
nodes.append(Node(2,1))
nodes.append(Node(3,1))
nodes.append(Node(4,2))
nodes.append(Node(5,2))
nodes.append(Node(6,3))
nodes.append(Node(7,3))
nodes.append(Node(8,4))
nodes.append(Node(9,4))


print('lca of 9 and 5 is {}'.format(LCA(9,5)))
print('lca of 1 and 9 is {}'.format(LCA(1,9)))
print('lca of 1 and 7 is {}'.format(LCA(1,7)))
print('LCA of 4 and 9 is {}'.format(LCA(4,9)))
print('LCA of 9 and 7 is {}'.format(LCA(9,7)))
print('LCA of 1 and 1 is {}'.format(LCA(1,1)))
'''