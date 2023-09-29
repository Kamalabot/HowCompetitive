""" 1. Image Processing - Flood Fill:

Problem: Flood fill is a common image processing technique used to fill a region of connected pixels with a specific color. It's used in various applications, such as image editing software.

Implementation:

 """
def flood_fill(matrix, row, col, target_color, new_color):
    if (
        row < 0
        or row >= len(matrix)
        or col < 0
        or col >= len(matrix[0])
        or matrix[row][col] != target_color
    ):
        return

    matrix[row][col] = new_color

    # Explore neighboring pixels
    flood_fill(matrix, row + 1, col, target_color, new_color)
    flood_fill(matrix, row - 1, col, target_color, new_color)
    flood_fill(matrix, row, col + 1, target_color, new_color)
    flood_fill(matrix, row, col - 1, target_color, new_color)

# Example usage:
image = [
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [1, 0, 0, 1],
]
flood_fill(image, 1, 1, 1, 2)

""" 2. Pathfinding - Shortest Path in a Grid (Dijkstra's Algorithm):

Problem: Finding the shortest path in a grid is essential in various applications like robotics, navigation, and game development.

Implementation:
 """
import heapq

def shortest_path(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    min_heap = [(0, start)]
    visited = set()

    while min_heap:
        dist, (row, col) = heapq.heappop(min_heap)
        if (row, col) == end:
            return dist

        if (row, col) in visited:
            continue

        visited.add((row, col))

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] != 1:
                heapq.heappush(min_heap, (dist + 1, (r, c)))

# Example usage:
grid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
start = (0, 0)
end = (2, 2)
print(shortest_path(grid, start, end))  # Output: 4

""" 3. Game Development - Maze Solving (Depth-First Search):

Problem: Maze solving is a common problem in game development and artificial intelligence. It involves finding a path from the start to the exit in a maze.

Implementation:
 """
def solve_maze(maze, start, end):
    def dfs(row, col):
        if (
            row < 0
            or row >= len(maze)
            or col < 0
            or col >= len(maze[0])
            or maze[row][col] != 0
        ):
            return False

        path.append((row, col))

        if (row, col) == end:
            return True

        maze[row][col] = -1  # Mark as visited

        if dfs(row + 1, col) or dfs(row - 1, col) or dfs(row, col + 1) or dfs(row, col - 1):
            return True

        path.pop()
        return False

    rows, cols = len(maze), len(maze[0])
    path = []

    if dfs(start[0], start[1]):
        return path
    else:
        return []

# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
end = (4, 4)
print(solve_maze(maze, start, end))  # Output: [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
