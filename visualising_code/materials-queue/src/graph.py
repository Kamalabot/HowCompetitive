# graph.py

from typing import MutableSet
from collections import deque
from math import inf as infinity
from typing import NamedTuple

import networkx as nx
# Commments for the below classes have been updated 
from queues import MutableMinHeap, Queue, Stack


class City(NamedTuple):
    # Creating a Type to accomodate city's details
    name: str
    country: str
    year: int | None
    latitude: float
    longitude: float

    @classmethod
    def from_dict(cls, attrs):
        # used for creating the City instance from the dictionary
        return cls(
            name=attrs["xlabel"],
            country=attrs["country"],
            year=int(attrs["year"]) or None,
            latitude=float(attrs["latitude"]),
            longitude=float(attrs["longitude"]),
        )


def load_graph(filename, node_factory):
    # read the dot file
    graph = nx.nx_agraph.read_dot(filename)
    # use the City.from_dict as node_factory
    nodes = {
        # create "city name":"City Instance" dictionary
        name: node_factory(attributes)
        for name, attributes in graph.nodes(data=True)
    }
    # return the nodes dictionary, Graph Instance
    return nodes, nx.Graph(
        # retrieve the City instances from nodes  
        (nodes[name1], nodes[name2], weights)
        # using the edges, weights from the graph read from dot file
        for name1, name2, weights in graph.edges(data=True)
    )


def breadth_first_traverse(graph, source, order_by=None):
    # Instantiate Queue Instance with the source City Object
    queue = Queue(source)
    # add the City object in the visited set
    visited = {source}
    # while there is value in the queue
    while queue:
        # dequeue the value in the queue, assign it to
        # node variable and keep yielding
        yield (node := queue.dequeue())
        # create list of neighbour City objects
        neighbors = list(graph.neighbors(node))
        # if order_by is provided
        if order_by:
            # sort the neighbors list
            neighbors.sort(key=order_by)
            # for each neighbour
        for neighbor in neighbors:
            # check if neighbour in visited set
            if neighbor not in visited:
                # if no then added neighbour to the visited set 
                visited.add(neighbor)
                # add the neighbour to the queue
                queue.enqueue(neighbor)


def breadth_first_search(graph, source, predicate, order_by=None):
    return search(breadth_first_traverse, graph, source, predicate, order_by)


def shortest_path(graph, source, destination, order_by=None):
    # uses the breadth first traversal to find the shortest distance
    # commenting on the lines that are different to the regular bfs algo
    queue = Queue(source)
    visited = {source}
    # creating a dictionary previous 
    previous = {}
    while queue:
        # dequeue and assign City instance to node
        node = queue.dequeue()
        # get their list of neighbours
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.enqueue(neighbor)
                # create a key value pair of neighbor City : visited_node City 
                previous[neighbor] = node
                # if neighbor is equal to destination
                if neighbor == destination:
                    # return the value by retracing
                    return retrace(previous, source, destination)
                # else keep traversing


def retrace(previous, source, destination):
    # used for retracing the path with a double queue
    path = deque()
    # create current var with destination City
    current = destination
    # as long as current is not source
    while current != source:
        # append the current City instance into path queue
        path.appendleft(current)
        # get parent of current from previous dictionary
        current = previous.get(current)
        # if current is None, means there is no parent
        if current is None:
            # return None
            return None
    # else it is source, append it to the left of deque
    path.appendleft(source)
    # return the list of City instances
    return list(path)


def connected(graph, source, destination):
    # check whether the source and destination are connected 
    # by trying to find the shortest path
    return shortest_path(graph, source, destination) is not None


def depth_first_traverse(graph, source, order_by=None):
    # instantiate Stack
    stack = Stack(source)
    # created visited set, to hold the City nodes traversed
    visited = set()
    while stack:
        # dequeue the top element in stack and assign to node var
        # check if the value is Not in visited set
        if (node := stack.dequeue()) not in visited:
            # yield the node
            yield node
            # add the node to visited set
            visited.add(node)
            # get the list of neighbours of the node
            neighbors = list(graph.neighbors(node))
            # order them if chosen feature is provided
            if order_by:
                neighbors.sort(key=order_by)
            # reverse the neighbors list and
            for neighbor in reversed(neighbors):
                # push the nodes in to the stack
                stack.enqueue(neighbor)


def recursive_depth_first_traverse(graph, source, order_by=None):
    # created the visited set
    visited = set()

    def visit(node):
        # Need to review and practice how yield works  
        yield node
        visited.add(node)
        neighbors = list(graph.neighbors(node))
        if order_by:
            neighbors.sort(key=order_by)
        for neighbor in neighbors:
            if neighbor not in visited:
                # need to practice how yield works
                yield from visit(neighbor)
    # returns a generator
    return visit(source)


def depth_first_search(graph, source, predicate, order_by=None):
    # use dfs to return the nodes traversed in the graph
    return search(depth_first_traverse, graph, source, predicate, order_by)


def search(traverse, graph, source, predicate, order_by=None):
    # use for loop to access the yielded instances 
    for node in traverse(graph, source, order_by):
        # what is predicate here?
        if predicate(node):
            return node


def dijkstra_shortest_path(graph, source, destination, weight_factory):
    previous = {}
    visited = set()
    # creating data structure to hold unvisited
    unvisited = MutableMinHeap()
    # enumerate all nodes in the graph
    for node in graph.nodes:
        # assign them the weight of infinity
        unvisited[node] = infinity
    # make the source weight as 0
    unvisited[source] = 0
    # as long as there are unvisited nodes
    while unvisited:
        # do multiple things in a single line below
        visited.add(node := unvisited.dequeue())
        # iterate over the neighbours and weights for the given node
        for neighbor, weights in graph[node].items():
            # if neighbor is not in visited
            if neighbor not in visited:
                # assign return value of weight_factory() to weight
                weight = weight_factory(weights)
                # updated the distance of the unvisited node
                new_distance = unvisited[node] + weight
                # check new distance is lesser than univisted[neighbor]
                if new_distance < unvisited[neighbor]:
                    # Update unvisited[node] = new distance
                    unvisited[neighbor] = new_distance
                    # make the node as part of previous dictionary
                    previous[neighbor] = node

    return retrace(previous, source, destination)
