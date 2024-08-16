import re
import os

# Input text containing the patterns and code snippets
input_text = """
Certainly! Below are the Python snippets extracted for each pattern, including the pattern name, introduction, sample problem statement, input and output, and a list of relevant LeetCode problems.

### 1. Modified Binary Search
```python
# Pattern: Modified Binary Search
# Introduction: 
# Adapts binary search to solve a wider range of problems, such as finding elements in rotated sorted arrays.
# Use this pattern for problems involving sorted or rotated arrays where you need to find a specific element.

# Sample Problem: 
# Find an element in a rotated sorted array.

# Example:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# Output: 4

# LeetCode Problems:
# 1. Search in Rotated Sorted Array (LeetCode #33)
# 2. Find Minimum in Rotated Sorted Array (LeetCode #153)
# 3. Search a 2D Matrix II (LeetCode #240)
```

### 2. Binary Tree Traversal
```python
# Pattern: Binary Tree Traversal
# Introduction: 
# Involves visiting all the nodes in a binary tree in a specific order (PreOrder, InOrder, PostOrder).

# Sample Problem:
# Perform inorder traversal of a binary tree.

# Example:
root = [1, None, 2, 3]
# Output: [1, 3, 2]

# LeetCode Problems:
# 1. PreOrder → Binary Tree Paths (LeetCode #257)
# 2. InOrder → Kth Smallest Element in a BST (LeetCode #230)
# 3. PostOrder → Binary Tree Maximum Path Sum (LeetCode #124)
```

### 3. Depth-First Search (DFS)
```python
# Pattern: Depth-First Search (DFS)
# Introduction: 
# A traversal technique that explores as far down a branch as possible before backtracking.

# Sample Problem:
# Find all paths from the root to leaves in a binary tree.

# Example:
root = [1, 2, 3, None, 5]
# Output: ["1->2->5", "1->3"]

# LeetCode Problems:
# 1. Clone Graph (LeetCode #133)
# 2. Path Sum II (LeetCode #113)
# 3. Course Schedule II (LeetCode #210)
```

### 4. Breadth-First Search (BFS)
```python
# Pattern: Breadth-First Search (BFS)
# Introduction: 
# A traversal technique that explores nodes level by level in a tree or graph.

# Sample Problem:
# Perform level-order traversal of a binary tree.

# Example:
root = [3, 9, 20, None, None, 15, 7]
# Output: [[3], [9, 20], [15, 7]]

# LeetCode Problems:
# 1. Binary Tree Level Order Traversal (LeetCode #102)
# 2. Rotting Oranges (LeetCode #994)
# 3. Word Ladder (LeetCode #127)
```

### 5. Matrix Traversal
```python
# Pattern: Matrix Traversal
# Introduction: 
# Involves traversing elements in a matrix using different techniques (DFS, BFS, etc.).

# Sample Problem:
# Perform flood fill on a 2D grid. Change all the cells connected to the starting cell to a new color.

# Example:
image = [[1,1,1], [1,1,0], [1,0,1]]
sr, sc = 1, 1
newColor = 2
# Output: [[2,2,2], [2,2,0], [2,0,1]]

# LeetCode Problems:
# 1. Flood Fill (LeetCode #733)
# 2. Number of Islands (LeetCode #200)
# 3. Surrounded Regions (LeetCode #130)
```

### 6. Backtracking
```python
# Pattern: Backtracking
# Introduction: 
# Explores all possible solutions and backtracks when a solution path fails.

# Sample Problem:
# Generate all permutations of a given list of numbers.

# Example:
nums = [1, 2, 3]
# Output: [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]]

# LeetCode Problems:
# 1. Permutations (LeetCode #46)
# 2. Subsets (LeetCode #78)
# 3. N-Queens (LeetCode #51)
```

### 7. Dynamic Programming Patterns
```python
# Pattern: Dynamic Programming Patterns
# Introduction: 
# Involves breaking down problems into smaller subproblems and solving them using a bottom-up or top-down approach.

# Sample Problem:
# Calculate the n-th Fibonacci number.

# Example:
n = 5
# Output: 5 (The first five Fibonacci numbers are 0, 1, 1, 2, 3, 5)

# LeetCode Problems:
# 1. Climbing Stairs (LeetCode #70)
# 2. House Robber (LeetCode #198)
# 3. Coin Change (LeetCode #322)
# 4. Longest Common Subsequence (LCS) (LeetCode #1143)
# 5. Longest Increasing Subsequence (LIS) (LeetCode #322)
# 6. Partition Equal Subset Sum (LeetCode #416)
```

These code snippets offer a starting point to practice and implement the patterns commonly asked in Sr. Data Analyst interviews.
"""

# Regular expression pattern to match each section
# pattern = r"### (\d+)\. (.*?)\n\n```python\n(.*?)```"
pattern = r"### (\d+)\. (.*?)```python\n(.*?)```"

# Create a directory to store the extracted files
# os.makedirs("extracted_patterns", exist_ok=True)

# Find all matches
matches = re.findall(pattern, input_text, re.DOTALL)
print(len(matches))
# Iterate over the matches and write each code snippet to a separate file
for i, pattern_name, code in matches:
    idx = int(i) + 8
    # Create a valid filename by removing invalid characters and replacing spaces with underscores
    filename = (
        re.sub(r"[^\w\s]", "", pattern_name).replace(" ", "_").replace("\n", "")
        + f"_{idx}"
        + ".py"
    )
    # print(f"filename: {filename}")
    # print(f"code: {code}")
    # print(f"pattern_name: {pattern_name}")
    # Write the code to a file
    with open(f"{filename}", "w") as file:
        file.write(code)

    print(f"Created file: {filename}")
