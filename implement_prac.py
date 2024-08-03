import logging
from typing import List

logging.basicConfig(format="%(levelname)s|%(message)s", level=logging.INFO,
                    force=True)

nodes = ['a', 'b', 'c', 'd', 'e']

vertex_list = [
    ['a', 'b'],
    ['a', 'd'],
    ['b', 'c'],
    ['b', 'e'],
    ['d', 'c']
    ]

adj_matrix = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0]
]

adj_list = [
    ['b', 'd'],
    ['c', 'a', 'e'],
    ['b', 'd'],
    ['a', 'c'],
    ['b']
]


def is_connected(node1: str, node2: str) -> bool:
    """Checks if two nodes are connected"""
    # enumerate over the vertex list
    for ele in vertex_list:
        # check if node1 is present
        if node1 in ele:
            # then check if node2 is present
            if node2 in ele:
                # return
                return True
    # if not present in any then return false
    return False


def adj_node(node: str, vert_list) -> List:
    # create a store
    store = []
    # enumerate the vertex list
    for ele in vert_list:
        # check if node in ele
        if node in ele:
            # idx of node
            idx = ele.index(node)
            # take the node in other idx
            store.append(ele[0]) if idx == 1 else \
                store.append(ele[1])
    # return the store
    return store


assert adj_node('a', vertex_list) == ['b', 'd']
assert adj_node('b', vertex_list) == ['a', 'c', 'e']

# assert is_connected('a', 'b'), 'not connected'
# assert is_connected('a', 'd'), 'not connected'


def mat_isconn(node1: str, node2: str, adj_mat: List[List]) -> bool:
    # find the index of node1 and node2 in given list
    idx_1 = nodes.index(node1)
    idx_2 = nodes.index(node2)

    # get value in adj_mat at idx1, idx2
    return True if adj_matrix[idx_1][idx_2] == 1 \
        else False


def mat_nodes(node: str, matrix: List[List]) -> List:
    # create a store
    store = []
    # get index of the node 
    idx = nodes.index(node)
    # get the idx list corresponding to above idx
    mat_list = matrix[idx]
    # enumerate on the acquired list
    for i, val in enumerate(mat_list):
        # check if val is 1
        if val == 1:
            # get the node at i in nodes and append it to store
            store.append(nodes[i])
    return store


assert mat_nodes('a', adj_matrix) == ['b', 'd']
assert mat_nodes('b', adj_matrix) == ['a', 'c', 'e']

# assert mat_isconn('a', 'b', adj_matrix), 'not connected'
# assert mat_isconn('a', 'd', adj_matrix), 'not connected'


def list_isconn(node1: str, node2: str, adj_list: List[List]) -> bool:
    # find index of node1
    idx = nodes.index(node1)
    # check if node2 in the elem found at adj_list[idx]
    return True if node2 in adj_list[idx] else False


def list_nodes(node: str, a_list: List[List]) -> List:
    # get the index of node in nodes
    idx = nodes.index(node)
    # get the corresponding list in a_list
    yourlist = a_list[idx]
    # return the list
    return yourlist 


assert list_nodes('a', adj_list) == ['b', 'd']
assert list_nodes('b', adj_list) == ['c', 'a', 'e']

# assert list_isconn('a', 'b', adj_list), 'not connected'
# assert list_isconn('a', 'd', adj_list), 'not connected'
