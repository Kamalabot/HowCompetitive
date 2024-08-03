# setting up logging
import logging

logging.basicConfig(format="%(message)s | %(asctime)s", dateformat="level=logging.WARNING, filename="graphlog.log", filemode='w')

import networkx as nx

# instantiating undirected graph
G = nx.Graph()

# adding node

G.add_node(2)

# adding node from list

G.add_nodes_from([5, 8])

# adding edges
G.add_edge(2,5)
G.add_edge(2,8)

# list nodes

logging.warning(list(G.nodes))

# list edges

logging.warning(list(G.edges))

# list adjacencies

logging.warning(list(G.adj[2]))

# provide degree

logging.warning(G.degree(2))
