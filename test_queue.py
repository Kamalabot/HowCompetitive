# implementing logger to retrieve the code checks
import logging
from typing import List

# create a logger
graphLog = logging.getLogger(__name__)
# setLevel to Debug
graphLog.setLevel(logging.DEBUG)
# create file handler
handler = logging.FileHandler(filename='graphlog.log',mode='w')
# setLevel on Handler
handler.setLevel(logging.INFO)
# create formatter
logformat = logging.Formatter(fmt='%(message)s:%(asctime)s_%(levelname)s',
                              datefmt='%b-%d-%H-%M')
# attach formatter to handler
handler.setFormatter(logformat)
# add handler to logger
graphLog.addHandler(handler)

# Implementing Graphs in 4 different methods, and 
# checking a node/ value is contained in a graph
# finding the adjacent node of a given graph
datapoints = ['a', 'b', 'c', 'd', 'e', 'f']
edges = [
    ['a', 'b'],
    ['a', 'c'],
    ['b', 'd'],
    ['a', 'd'],
    ['b', 'e'],
    ['e', 'f'],
    ['c', 'f'],
]


# def adjacent_node(node: str, edgeList: List[List[str]]):
#     # create list to hold result
#     result = []
#     # loop on the edge list
#     for edg in edgeList:
#         # try checking if node in edge
#         if node in edg:
#             # get idx of node and take the other element 
#             result.append(edg[0]) if edg.index(node) == 1 else result.append(edg[1])
#     # return result
#     return result
# 
# 
# def isConnected(node1: str, node2: str):
#     # loop over the edges
#     for edg in edges:
#         # check if node1 and node2 are present
#         if node1 in edg and node2 in edg:
#             return True
#     # complete the entire edge list and return False
#     return False

# graphLog.info(adjacent_node('a', edges))  # b, c, d
# graphLog.info(adjacent_node('e', edges))  # b, f
# graphLog.info(adjacent_node('b', edges))  # e, d, a

# graphLog.warning(isConnected('a', 'b'))  # True
# graphLog.warning(isConnected('d', 'b'))  # True
# graphLog.warning(isConnected('e', 'a'))  # False
# working on the adjacency matrix 
edges = [
    ['a', 'b'],
    ['a', 'c'],
    ['b', 'd'],
    ['a', 'd'],
    ['b', 'e'],
    ['e', 'f'],
    ['c', 'f'],
]

edgeMatrix = [
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0],
] 


# def adjacent_node(node: str, matrix: List[List[int]]):
#     # make index map of nodes
#     idx_map = dict()
#     for ind, ele in enumerate(datapoints):
#         idx_map[ele] = ind
#     # graphLog.info(idx_map)
#     # create list to collect nodes
#     result = []
#     # get idx of node, use that select element on edgematrix and loop on it
#     for ind, ids in enumerate(matrix[idx_map[node]]):
#         # chek if elem is 1
#         if ids == 1:
#             # append the node at the 'ind' by using idx_map.keys() as list
#             result.append(list(idx_map.keys())[ind])
#     # return result
#     return result
 
 
# def isConnected(node1: str, node2: str, matrix: List[List[int]]):
#     # create the idx_map of the node and its position
#     idx_map = dict()
#     # loop over the datapoints
#     for ind, val in enumerate(datapoints):
#         idx_map[val] = ind
#     # get the indices of node1 and node2 
#     x, y = idx_map[node1], idx_map[node2]
#     # return True if it is 1 at indices inside matrix else return False
#     if matrix[x][y] == 1:
#         return True
#     else:
#         return False


# graphLog.info(adjacent_node('a', edgeMatrix))  # b, c, d
# graphLog.info(adjacent_node('e', edgeMatrix))  # b, f
# graphLog.info(adjacent_node('b', edgeMatrix))  # e, d, a
 
# graphLog.warning(isConnected('e', 'f', edgeMatrix))  # True
# graphLog.warning(isConnected('a', 'f', edgeMatrix))  # False

# Implementing the Graph based on Nodes datastructure

class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []

    def connect(self, other: "Node"):
        self.nodes.append(other)
        other.nodes.append(self)

    def __str__(self):
        # return the node value along with the values of nodes connected with it
        return f"{self.value} is connected with {','.join([ele.value for ele in self.nodes])}"

    def connecteNodes(self):
        "Return the value of connected nodes"
        return ",".join([ele.value for ele in self.nodes])

    def isConnected(self, other: 'Node'):
        "check if other node is self.nodes list"
        return other in self.nodes


A = Node('a')
F = Node('f')
B = Node('b')
C = Node('c')
D = Node('d')
E = Node('e')

A.connect(B)
A.connect(C)
C.connect(B)
D.connect(C)
B.connect(E)
A.connect(D)

graphLog.info(A)
graphLog.info(B)

graphLog.warning(A.connecteNodes())
graphLog.warning(B.connecteNodes())
graphLog.warning(E.connecteNodes())

graphLog.info(E.isConnected(A))  # False
graphLog.info(E.isConnected(B))  # True