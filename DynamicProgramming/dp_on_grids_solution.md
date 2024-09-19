Here are two additional dynamic programming (DP) problems on grids, along with examples and code solutions:

---

## **1. Minimum Path Sum**

### **Problem Statement:**

Given a 2D grid filled with non-negative numbers, find a path from the top-left corner to the bottom-right corner that minimizes the sum of the numbers along the path. You can only move either down or right at any point in time.

### **Example 1**:

```plaintext
Input:
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]

Output: 7

Explanation: 
The path is 1 → 3 → 1 → 1 → 1, and the sum is 7.
```

### **Approach**:

- Use dynamic programming to build a 2D DP table where `dp[i][j]` represents the minimum sum to reach cell `(i, j)`.
- The DP transition is based on moving either from the left or from above the current cell.

### **Code Solution** (Python):

```python
def minPathSum(grid):
    if not grid:
        return 0

    m, n = len(grid), len(grid[0])

    # Initialize the DP table with the first cell
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[m - 1][n - 1]

# Example usage
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))  # Output: 7
```

---

## **2. Unique Paths II (With Obstacles)**

### **Problem Statement:**

You are given a 2D grid representing a robot's environment, where some cells are obstacles, and others are free. The robot can only move down or right. Find the number of unique paths that the robot can take to reach the bottom-right corner from the top-left corner. If the robot encounters an obstacle (`1`), it cannot pass through that cell. Empty cells are marked as `0`.

### **Example 1**:

```plaintext
Input:
obstacleGrid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]

Output: 2

Explanation: 
There are two possible paths to reach the bottom-right corner:
1. Right → Right → Down → Down
2. Down → Down → Right → Right
```

### **Example 2**:

```plaintext
Input:
obstacleGrid = [
  [0, 1],
  [0, 0]
]

Output: 1
```

### **Approach**:

- Use a DP table `dp[i][j]` where each cell holds the number of unique paths to reach `(i, j)`.
- If there's an obstacle at a cell, set `dp[i][j] = 0` (no paths can pass through).
- The robot can only move from the left or above, so the DP transition is based on the sum of `dp[i-1][j]` and `dp[i][j-1]`.

### **Code Solution** (Python):

```python
def uniquePathsWithObstacles(obstacleGrid):
    if not obstacleGrid or obstacleGrid[0][0] == 1:
        return 0

    m, n = len(obstacleGrid), len(obstacleGrid[0])

    # Initialize the DP table
    dp = [[0] * n for _ in range(m)]

    # Starting position
    dp[0][0] = 1

    # Fill the first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] if obstacleGrid[0][j] == 0 else 0

    # Fill the first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] if obstacleGrid[i][0] == 0 else 0

    # Fill the rest of the DP table
    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

    return dp[m - 1][n - 1]

# Example usage
obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
print(uniquePathsWithObstacles(obstacleGrid))  # Output: 2
```

---

### Summary of Differences:

1. **Minimum Path Sum**: Focuses on finding the minimal sum of a path from the top-left to the bottom-right, allowing only down or right moves. It uses dynamic programming to accumulate minimum path sums.

2. **Unique Paths II**: Focuses on counting the number of distinct paths to reach the bottom-right, given obstacles. It also uses dynamic programming, but the emphasis is on counting rather than minimizing a cost.
