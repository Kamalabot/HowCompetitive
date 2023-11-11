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


print(isConnected('a', 'b'))  # True
print(isConnected('a', 'c'))  # False
print(isConnected('d', 'c'))  # True 
print(isConnected('b', 'c'))  # True
