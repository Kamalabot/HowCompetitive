""" 1. Binary Search:
Binary search is an efficient algorithm for finding a specific element in a sorted list. It repeatedly divides the search interval in half until the element is found or the interval becomes empty.

 """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Search the right half
        else:
            right = mid - 1  # Search the left half

    return -1  # Element not found

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found.")

""" 2. Depth-First Search (DFS):
DFS is used to traverse or search for nodes in a graph or tree structure by exploring as far as possible along each branch before backtracking.

 """
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D', 'E'])
g.add_edge('C', ['A', 'F'])
g.add_edge('D', ['B'])
g.add_edge('E', ['B', 'F'])
g.add_edge('F', ['C', 'E'])

print("DFS traversal starting from 'A':")
g.dfs('A')
Save to grepper
3. Breadth-First Search (BFS):
BFS is another traversal algorithm used to explore or search for nodes in a graph or tree structure. It explores all neighbors at the current depth before moving to the next level.

python
Copy code
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Example usage:
g = Graph()
g.add_edge('A', ['B', 'C'])
g.add_edge('B', ['A', 'D', 'E'])
g.add_edge('C', ['A', 'F'])
g.add_edge('D', ['B'])
g.add_edge('E', ['B', 'F'])
g.add_edge('F', ['C', 'E'])

print("BFS traversal starting from 'A':")
g.bfs('A')
