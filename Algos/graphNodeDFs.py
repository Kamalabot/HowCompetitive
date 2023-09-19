class Graph:
  def __init__(self, data, neighbors = None):
    if neighbors is None:
      neighbors = []
    self.data = data
    self.neighbors = neighbors
    
def graphDfs(vertex, visited = None):
  if visited is None:
    visited = set()
  if vertex is None or vertex in visited:
    return
  else:
    print(vertex.data)
    visited.add(vertex)
    for neighbor in vertex.neighbors:
      graphDfs(neighbor, visited)
    
# Time complexity:  Directed graph: O(|V|+|E|) 
#                   Undirected graph: O(|V|+2|E|) which is also considered O(|V|+|E|) by removing the constant
#                   where |V| is the number of vertices and |E| is the number of edges
# Space complexity: O(|V|) where |V| is the number of vertices
#                   the additional space comes from the maximum call stack size