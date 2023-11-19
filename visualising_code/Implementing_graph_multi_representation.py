# The file contains the implementation of Graphs in 
# different ways, following the coderbyte video
from typing import List

vertices = ['a', 'b', 'c', 'd', 'e']

edges = [['a', 'b'],
         ['a', 'd'],
         ['b', 'c'],
         ['c', 'd'],
         ['c', 'e'],
         ['d', 'e']]

# Why implement? To find adjacent nodes to a given node


def adjancentNode(node: str, edges: List[List[str]]) -> List[str]:
    # Create result list to hold output 
    result = []
    # Look at the each edge in edges list 
    for edg in edges:
        # Check if node we want is in the element then 
        if node in edg:
            # push the other node in the list
            if edg.index(node) == 1:
                result.append(edg.pop(0))
            else:
                result.append(edg.pop(1))
 
    return result


def adjacent_node(node: str, edgeList: List[List[str]]):
    # create list to hold result
    result = []
    # loop on the edge list
    for edg in edgeList:
        # try checking if node in edge
        if node in edg:
            # get idx of node and take the other element 
            result.append(edg[0]) if edg.index(node) == 1 else result.append(edg[1])
    # return result
    return result

# print(adjancentNode('a', edges)) # ['b', 'd']
# print(adjancentNode('c', edges)) # ['b', 'd', 'e']


# def isConnected(node1: str, node2: str) -> bool:
#     # Create a result list to hold bools
#     result = []
#  
#     # Loop over the list of edges
#     for edg in edges:
#         print(edg)
#         # check if node1 is present in the edge
#         if node1 in edg:
#             # if present, then check if node2 is present that edge
#             if node2 in edg:
#                 # append True
#                 result.append(True)
#             else: 
#                 # else return False
#                 result.append(False)
#         else:
#             result.append(False)
#     print(result)
#     return any(result)

# Pseudo code itself has to be modified when it comes to the logic 

def isConnected(node1: str, node2: str) -> bool:
    result = []
    for edg in edges:
        # print(edg)
        if node1 in edg and node2 in edg:
            result.append(True)
        result.append(False)

    return any(result)


#  print(isConnected('a', 'b', vertices, adj_matrix))  # True
#  print(isConnected('a', 'c', vertices, adj_matrix))  # False
#  print(isConnected('d', 'c', vertices, adj_matrix))  # True 
#  print(isConnected('b', 'c', vertices, adj_matrix))  # True
 
# Adjancency Matrix : A 2 dimensional Array 

adj_matrix = [
    [0, 1, 0, 1, 0],  # rep a node
    [0, 0, 1, 0, 0],  # rep b node
    [0, 1, 0, 1, 1],  # rep c node
    [1, 0, 1, 0, 1],  # rep d node
    [0, 0, 1, 1, 0],  # rep e node
]


def am_adjNode(node: str, adj_mat: List[List[int]], node_list: List[int]) -> List[int]:
    # find the index of node in the node_list 
    # idx = node_list.index(node) # This will have O(n) complexity, which can be reduced to O(1) using a dict

    # Another way to find node in the list, is first creating dictionary
 
    node_dict = dict() 
    for ind, elm in enumerate(node_list):
        node_dict[elm] = ind
    idx = node_dict[node]  # This will be O(1) complexity 

    # create a result list
    result = []

    # Go to the corresponding sub-array in the adj_matrix
    for ind, elem in enumerate(adj_mat[idx]):
        # Find where the elements are 1
        if elem == 1:
            # append the value of element in that index to the result
            result.append(node_list[ind])
    # return result
    return result


# print(am_adjNode('a', adj_matrix, vertices))  # ['b', 'd']
# print(am_adjNode('c', adj_matrix, vertices))  # ['b', 'd', 'e']


def am_isCon(node1: str, node2: str, node_list: List[str], adj_mat: List[List[int]]) -> bool:
    node_dict = dict()
    for ind, ele in enumerate(node_list):
        node_dict[ele] = ind
    
    # Find the indices of both the nodes in the node_list
    x, y = node_dict[node1], node_dict[node2]
    # Go to the corresponding sub_array, and the element location.
    chk = adj_mat[x][y]
    # If there is a 1 then connected (True)
    return chk == 1
    # return the results


# print(am_isCon('a', 'b', vertices, adj_matrix))  # True
# print(am_isCon('a', 'c', vertices, adj_matrix))  # False
# print(am_isCon('d', 'c', vertices, adj_matrix))  # True 
# print(am_isCon('b', 'c', vertices, adj_matrix))  # True

# Adjacency List implementation: Will building a Node Closs, Graph Class, adding the edgeList for the connections and then work on the functions 


class Node:

    def __init__(self, value: str | int | float) -> None:
        self.color = None
        self.value = value
        self.edgeList = []
 
    def connect(self, node) -> None:  # Connections or the edges are taken care in the nodes itself.
        self.edgeList.append(node)
        node.edgeList.append(self)

    def __repr__(self):
        return self.value 

    def __str__(self):
        connections = [str(self.value) + " <-> " + str(node.value) for node in self.edgeList]
        return f"{connections}"

    def getEdgeList(self):
        return self.edgeList

    def isConnected(self, node):
        return node in self.edgeList


class Graph:

    def __init__(self, nodes: List[Node]) -> None:
        self.nodes = [node for node in nodes]

    def __str__(self):
        return f"{[node.value for node in self.nodes]}"
    
    def addToGraph(self, node:Node) -> None:
        self.nodes.append(node)

    def isBipartite(self):
        visited = set()
        # Graph is made of many nodes, try checking 
        # each node and assign legal coloring
        for node in self.nodes:
            if node not in visited:
                if self.assignLegalColor(node, visited):
                    print("Graph is bi-partite")
                    # filter the red team
                    red_team = [node.value for node in self.nodes if node.color == 'red']
                    # filter the blue team
                    blue_team = [node.value for node in self.nodes if node.color == 'blue']
                    print("red_team: ", red_team)
                    print("blue_team: ", blue_team)
                else:
                    print("Graph is not bi-partite")

    @staticmethod
    def assignLegalColor(start, visitedSet):
        # the check if start is in visitedSet, is done down the code
        # if start in visitedSet:
            # Yes then return
            # return
        # print the node value for reference
        # print(f"visiting {start.value}")
        # if the start.color is none then assign red
        if start.color is None:
            start.color = 'red' 
        # add the start node to visited set
        visitedSet.add(start)
        
        # enumerate each node in edgeList of start node
        for node in start.edgeList:
            # Check if node is in visited set
            if node not in visitedSet:
                # assign color to the adjacencies
                node.color = 'blue' if start.color == 'red' else 'red'
                # print(f"Assigned {node.color} to {node.value}")
                # call assignLegalColor with each node
                if Graph.assignLegalColor(node, visitedSet) is False:
                    return False
                # the call will initiate the depth first traversal
            else:
                # node is in visited. Check if color same as start color
                if node.color == start.color:
                    # yes then return false
                    return False
        return True


# Creating the nodes
nodeA = Node('a')
nodeB = Node('b')
nodeC = Node('c')
nodeD = Node('d')
nodeE = Node('e')

# print(nodeA, nodeE)

graph = Graph(nodes=[nodeA, nodeB, nodeC, nodeD, nodeE])

# print(graph)

# repr(graph)

# Creating the connections, there will be only 5 as these are undirected
nodeA.connect(nodeB)
nodeA.connect(nodeD)
nodeC.connect(nodeD)
nodeC.connect(nodeB)
nodeC.connect(nodeE)

# print("After creating connections")
# print(repr(nodeA))
# print(repr(nodeB))
# print(repr(nodeC))
# print(repr(nodeD))
# print(repr(nodeE))
# 
# 
# print(nodeA.getEdgeList())
# print(nodeB.getEdgeList())
# 
nodeF = Node('f')
graph.addToGraph(nodeF)

# print("Aftering addin a new node")
# print(graph)
# 
# print(nodeD.isConnected(nodeA))  # True
# print(nodeA.isConnected(nodeC))  # False
# print(nodeC.isConnected(nodeB))  # True
# print(nodeF.isConnected(nodeE))  # False

# This is not a Binary Tree. Its a Graph.
# Create the nodes first.
# Children has to be added later. They children are just attributes

jack = Node(value="jack")
emily = Node(value="emily")
lucy = Node(value="lucy")
david = Node(value="david")
brian = Node(value="brian")
chris = Node(value="chris")
jose = Node(value="jose")
paul = Node(value="paul")


# Initiate a Graph Object

students = Graph([jack, emily, lucy, david, brian, chris, jose, paul])

# print(students)

david.connect(lucy)
david.connect(jose)
david.connect(chris)
lucy.connect(brian)
lucy.connect(emily)
emily.connect(jack)
jose.connect(paul)
paul.connect(chris)
chris.connect(brian)
brian.connect(jack)
# below connectivity will break the bi-partite graph
# lucy.connect(chris)


# print(david)
# print(paul)

print(students.isBipartite())