""" Breadth-First Search (BFS):

BFS is used to explore or traverse a graph level by level, starting from a specified source vertex. It's commonly used for finding the shortest path in an unweighted graph.

 """
 
from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend(self.graph[vertex])

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS starting from vertex 2:")
g.bfs(2)

""" Depth-First Search (DFS):

DFS is used to explore or traverse a graph by visiting as far as possible along a branch before backtracking. It's often used for tasks like topological sorting and cycle detection.

 """class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("DFS starting from vertex 2:")
g.dfs(2, set())

""" Dijkstra's Algorithm:

Dijkstra's algorithm is used to find the shortest path between a source vertex and all other vertices in a weighted graph.

 """
 import heapq

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))

    def dijkstra(self, start):
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances

# Example usage
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 2)
g.add_edge('B', 'C', 5)
g.add_edge('B', 'D', 10)
g.add_edge('C', 'D', 3)
g.add_edge('D', 'E', 7)
g.add_edge('E', 'A', 8)
g.add_edge('E', 'C', 6)

distances = g.dijkstra('A')
print("Shortest distances from vertex A:")
for vertex, distance in distances.items():
    print(f"To {vertex}: {distance}")
