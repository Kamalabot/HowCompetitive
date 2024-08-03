class Graph:
  def __init__(self, adjList = None):
    if adjList is None:
      adjList = []
    self.adjList = adjList
    
def graphDfs(graph, node, visited = None):
  if visited is None:
    visited = set()
  if node in visited:
    return
  else:
    print(node)
    visited.add(node)
    for neighbor in graph.adjList[node]:
      graphDfs(graph, neighbor, visited)
      
# Time complexity:  Directed graph: O(|V|+|E|) 
#                   Undirected graph: O(|V|+2|E|) which is also considered O(|V|+|E|) by removing the constant
#                   where |V| is the number of vertices and |E| is the number of edges
# Space complexity: O(|V|) where |V| is the number of vertices
#                   the additional space comes from the maximum call stack size