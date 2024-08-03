class FullNode:
    def __init__(self, val) -> None:
        self.val = val
        self.edgeList = []

    def connect(self, node):
        self.edgeList.append(node)
        # node.edgeList.append(self)

    def __repr__(self) -> str:
        return self.val

    def getEdges(self):
        return f'{self.val} is connnected with {self.edgeList}'
 
    def isConnected(self, node):
        return node in self.edgeList

    def gen_vertex_list(self, node_list):
        vert_list = []  # create a list store
        # get index of self
        self_idx = node_list.index(self.val)
        # traverse the edjelist
        for edge in self.edgeList:
            # get index of the edge in node_list
            idx = node_list.index(edge.val)
            # append the edge connectivity to vert_list
            vert_list.append([self_idx, idx])
        return vert_list

    def get_adj_list(self):
        return [node.val for node in self.edgeList]


lst = 'i,f,t,h,u,s'.split(',')
print(lst)
i = FullNode(lst[0])
f = FullNode(lst[1])
t = FullNode(lst[2])
h = FullNode(lst[3])
u = FullNode(lst[4])
s = FullNode(lst[5])

i.connect(f)
i.connect(t)
t.connect(h)
f.connect(u)
u.connect(s)

print(i.getEdges())
print(f.getEdges())
print(t.getEdges())
print(h.getEdges())
print(u.getEdges())
print(s.getEdges())

print(i.get_adj_list())


def traverse_new(node):
    tk = [node]
    while len(tk) > 0:
        curr = tk.pop(0)
        print(curr.val)
        if len(curr.edgeList) > 0:
            [tk.insert(0, elem) for elem in curr.edgeList]
    return
    

def build_vertex_list(node, node_list):
    vert_list = []  # Get a store
    tk = [node]
    while len(tk) > 0:
        curr = tk.pop(0)
        vertices = curr.gen_vertex_list(node_list)
        vert_list.extend(vertices)
        if len(curr.edgeList) > 0:
            [tk.insert(0, elem) for elem in curr.edgeList]
    return vert_list


def build_adj_list(node):
    adj_list = []  # Get a store
    tk = [node]
    while len(tk) > 0:
        curr = tk.pop(0)
        vertices = curr.get_adj_list()
        adj_list.append(vertices)
        if len(curr.edgeList) > 0:
            [tk.insert(0, elem) for elem in curr.edgeList]
    return adj_list


list_len = len(lst)
adj_matrix = [[0 for _ in range(list_len)]
              for _ in lst]


def gen_adj_matrix(node, adj_matrix, node_list):
    vertices = node.gen_vertex_list(node_list)
    new_am = adj_matrix
    for vert in vertices:
        print(vert)
        new_am[vert[0]][vert[1]] = 1
    return new_am


# print(i.gen_vertex_list(lst))
# print(build_vertex_list(i, lst))
# print(build_adj_list(i))
print(gen_adj_matrix(i, adj_matrix, lst))
