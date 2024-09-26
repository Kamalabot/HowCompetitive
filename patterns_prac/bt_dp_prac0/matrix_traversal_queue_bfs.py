from collections import deque


# original flood_fill is a dfs traversal recursive solution
# below is BFS queue based traversal solution
def flood_fill(image, sr, sc, new_color):
    original_color = image[sr][sc]
    if original_color == new_color:
        return image

    # Initialize the queue for BFS
    queue = deque([(sr, sc)])
    image[sr][sc] = new_color

    # Define directions for 4-way traversal (up, down, left, right)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Perform BFS
    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < len(image)
                and 0 <= nc < len(image[0])
                and image[nr][nc] == original_color
            ):
                image[nr][nc] = new_color
                queue.append((nr, nc))

    return image
