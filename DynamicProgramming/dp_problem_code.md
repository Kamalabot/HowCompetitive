Dynamic Programming (DP) solutions can be broadly categorized into the following types:

1. **Top-Down Approach (Memoization)**:
   
   - **Description**: A recursive approach that solves the problem by breaking it down into smaller subproblems and storing their results to avoid redundant computations.
   - **Use Case**: When recursive solutions are straightforward, but redundant calculations cause inefficiency.

2. **Bottom-Up Approach (Tabulation)**:
   
   - **Description**: An iterative approach that solves smaller subproblems first and uses their results to build up solutions to larger subproblems.
   - **Use Case**: When a problem can be solved iteratively and dependencies between subproblems are well understood.

3. **Space Optimization**:
   
   - **Description**: An optimization of the Bottom-Up approach where only necessary states are kept in memory, often reducing space complexity from O(n) to O(1).
   - **Use Case**: When space usage is critical, and not all previous results need to be stored.

4. **Bitmask DP**:
   
   - **Description**: Uses bitmasks to represent subsets, often used for problems involving permutations or combinations of sets.
   - **Use Case**: Useful in problems like Traveling Salesman Problem, subset partitioning, and state tracking.

5. **Digit DP**:
   
   - **Description**: A specialized DP technique used for counting numbers within a range that satisfies certain digit properties.
   - **Use Case**: Problems involving digit constraints, like counting numbers with specific digits.

6. **Knuth Optimization**:
   
   - **Description**: Optimizes certain DP problems, particularly in matrix chain multiplication, by reducing the search space of transitions.
   - **Use Case**: Problems where transitions follow specific convexity or monotonicity conditions.

7. **Convex Hull Trick/Line DP**:
   
   - **Description**: A technique used for optimizing DP problems involving linear functions, particularly for minimizing or maximizing cost functions.
   - **Use Case**: Used in problems like optimizing sums, costs, or other linear functions.

These variations allow DP to tackle a wide array of optimization and combinatorial problems effectively.

Dynamic Programming (DP) is essentially about breaking a complex problem into smaller, manageable subproblems, solving them once, and using their solutions to build the answer to the original problem. Here's an intuitive framework on the steps typically followed in DP:

### Intuitive Framework for Dynamic Programming

1. **Define the Subproblems**:
   
   - Identify what the smaller subproblems are. Think about how the problem can be divided into simpler instances of the same problem.

2. **Identify the Recurrence Relation**:
   
   - Establish how the solution to the current subproblem can be derived using the solutions of smaller subproblems (usually via a recursive formula).

3. **Decide the Approach (Top-Down vs. Bottom-Up)**:
   
   - **Top-Down (Memoization)**: Use recursion and cache results to avoid redundant calculations.
   - **Bottom-Up (Tabulation)**: Use iteration to solve subproblems first, storing the results in a table or array.

4. **Initialize Base Cases**:
   
   - Define the simplest cases with known answers, which serve as the foundation for solving larger subproblems.

5. **Build the Solution**:
   
   - Use the recurrence relation iteratively or recursively to solve each subproblem, moving towards the final solution.

6. **Optimize (if possible)**:
   
   - Simplify space or time complexity if there are redundant states or unnecessary calculations. Use techniques like space optimization to reduce memory usage.

7. **Extract the Final Answer**:
   
   - Retrieve the solution to the original problem from your data structure (array, table, etc.).

### Example of Application:

- **Problem**: Fibonacci Sequence
  - **Subproblems**: Find `F(n-1)` and `F(n-2)`.
  - **Recurrence Relation**: `F(n) = F(n-1) + F(n-2)`.
  - **Approach**: Bottom-Up with array initialization.
  - **Base Cases**: `F(0) = 0`, `F(1) = 1`.
  - **Build Solution**: Iterate from 2 to `n`, filling up values in an array.
  - **Extract Answer**: Return the `n`th value.

This framework helps guide you through the structured approach of breaking down and systematically solving complex problems using DP.

Here are the extracted dynamic problem patterns along with their example LeetCode problems and a solution for the first problem under each topic.

### 1. **Fibonacci Sequence**

**Problem**: LeetCode 70: Climbing Stairs

```python
# Problem: Climbing Stairs (LeetCode 70)
# The number of ways to reach the nth step can be solved using a dynamic programming approach,
# similar to the Fibonacci sequence, where the number of ways to reach the nth step depends
# on the number of ways to reach the (n-1)th and (n-2)th steps.

def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    # dp[i] represents the number of ways to reach the ith step
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    # Build the solution for each step
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # The current step depends on the previous two steps

    return dp[n]

# Example to test the solution
print(climbStairs(5))  # Output: 8
```

---

### 2. **Kadane's Algorithm**

**Problem**: LeetCode 53: Maximum Subarray

```python
# Problem: Maximum Subarray (LeetCode 53)
# Using Kadane's Algorithm to find the maximum sum of a contiguous subarray.
# We maintain a running sum and update the maximum sum when necessary.

def maxSubArray(nums: list[int]) -> int:
    current_sum = max_sum = nums[0]

    # Traverse the array to find the maximum sum subarray
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)  # Either start new subarray or continue
        max_sum = max(max_sum, current_sum)  # Update the max sum if current is greater

    return max_sum

# Example to test the solution
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6
```

---

### 3. **0/1 Knapsack**

**Problem**: LeetCode 416: Partition Equal Subset Sum

```python
# Problem: Partition Equal Subset Sum (LeetCode 416)
# We use dynamic programming to check if we can partition the array into two subsets
# with equal sum.

def canPartition(nums: list[int]) -> bool:
    total_sum = sum(nums)

    # If the total sum is odd, we cannot partition it into two equal subsets
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True

    # Process each number in nums
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]  # Include current number in the subset or not

    return dp[target]

# Example to test the solution
print(canPartition([1, 5, 11, 5]))  
# Output: True
```

---

### 4. **Unbounded Knapsack**

**Problem**: LeetCode 322: Coin Change

```python
# Problem: Coin Change (LeetCode 322)
# This is a variation of the Unbounded Knapsack problem where
# we want to minimize
# the number of coins to make up a given amount.

def coinChange(coins: list[int], amount: int) -> int:
    # dp[i] represents the minimum coins needed to make the amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins to make 0 amount

    # Process each coin and update the dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)  # Choose the minimum coins

    return dp[amount] if dp[amount] != float('inf') else -1

# Example to test the solution
print(coinChange([1, 2, 5], 11))  # Output: 3
```

---

### 5. **Longest Common Subsequence (LCS)**

**Problem**: LeetCode 1143: Longest Common Subsequence

```python
# Problem: Longest Common Subsequence (LeetCode 1143)
# We use dynamic programming to find the longest subsequence 
# common between two strings.

def longestCommonSubsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # If characters match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # Else, take the max of adjacent cells

    return dp[m][n]

# Example to test the solution
print(longestCommonSubsequence("abcde", "ace"))  
# Output: 3
```

---

### 6. **Longest Increasing Subsequence (LIS)**

**Example Problem:**  
**LeetCode 300: Longest Increasing Subsequence**

```python
# Problem: Longest Increasing Subsequence

def lengthOfLIS(nums):
    # DP array to store the length of the longest increasing subsequence till each index
    dp = [1] * len(nums)

    # Iterate over the array to build up the dp array
    for i in range(1, len(nums)):
        for j in range(i):
            # If the current element is greater than 
            # the previous element
            if nums[i] > nums[j]:
                # Update the dp array by taking the max of current and the subsequence length from j
                dp[i] = max(dp[i], dp[j] + 1)

    # Return the maximum value in the dp array as the result
    return max(dp)

# Example check
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(lengthOfLIS(nums))  
# Output: 4 (Subsequence: [2, 3, 7, 101])
```

---

### 7. **Palindromic Subsequence**

**Example Problem:**  
**LeetCode 516: Longest Palindromic Subsequence**

```python
# Problem: Longest Palindromic Subsequence

def longestPalindromeSubseq(s):
    # Length of the string
    n = len(s)
    # DP table where dp[i][j] represents the longest palindromic subsequence in s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table in a bottom-up manner
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # If characters at i and j are the same, extend the palindrome
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The answer is the full string's longest palindromic subsequence
    return dp[0][n - 1]

# Example check
s = "bbbab"
print(longestPalindromeSubseq(s))  
# Output: 4 (Subsequence: "bbbb")
```

What I observe is the subsequence need not be continous

---

### 8. **Edit Distance**

**Example Problem:**  
**LeetCode 72: Edit Distance**

```python
# Problem: Edit Distance (Levenshtein Distance)

def minDistance(word1, word2):
    # Get the lengths of both words
    m, n = len(word1), len(word2)
    # DP table where dp[i][j] represents the edit distance between word1[:i] and word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the table
    for i in range(m + 1):
        dp[i][0] = i  
# Distance of transforming word1[:i] to an empty word
    for j in range(n + 1):
        dp[0][j] = j  
# Distance of transforming an empty word 
# to word2[:j]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Characters match, no extra cost
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1  
            # Insert, Delete, Replace

    # Return the edit distance for the full words
    return dp[m][n]

# Example check
word1 = "horse"
word2 = "ros"
print(minDistance(word1, word2))  # Output: 3
```

---

### 9. **Subset Sum**

**Example Problem:**  
**LeetCode 416: Partition Equal Subset Sum**

Solution looks same as the Knapsack problem

```python
# Problem: Partition Equal Subset Sum

def canPartition(nums):
    total_sum = sum(nums)
    # If the total sum is odd, we cannot partition it into two equal subsets
    if total_sum % 2 != 0:
        return False

    # Target sum for each subset
    target = total_sum // 2
    n = len(nums)
    # DP array to store whether a sum is possible
    dp = [False] * (target + 1)
    dp[0] = True  # A sum of 0 is always possible

    # Process each number in the array
    for num in nums:
        # Traverse backwards to prevent overwriting
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]

    # The result is whether we can form the target sum
    return dp[target]

# Example check
nums = [1, 5, 11, 5]
print(canPartition(nums))  # Output: True
```

---

### 10. **String Partition**

**Example Problem:**  
**LeetCode 139: Word Break**

```python
# Problem: Word Break

def wordBreak(s, wordDict):
    # Convert wordDict to a set for faster lookup
    word_set = set(wordDict)
    # DP array where dp[i] means s[:i] can be 
    # segmented into words in wordDict
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Empty string can be segmented

    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[len(s)]

# Example check
s = "leetcode"
wordDict = ["leet", "code"]
print(wordBreak(s, wordDict))  # Output: True
```

---

### 11. **Catalan Numbers**

**Example Problem:**  

Catalan numbers are directly related to the count of distinct Binary Search Trees (BSTs) that can be formed with `n` distinct nodes. 

For a given `n`, the nth Catalan number represents the number of unique ways to arrange nodes in a BST. This is because each distinct BST configuration corresponds to a unique ordering of left and right subtrees, which can be recursively counted using Catalan numbers. The recursive nature of Catalan numbers perfectly models the recursive structure of BSTs, where each node's left and right subtrees can independently form valid BSTs from the remaining nodes.

**LeetCode 96: Unique Binary Search Trees**

```python
# Problem: Unique Binary Search Trees (Catalan Number application)

def numTrees(n):
    # DP array to store the number of unique BSTs for each number of nodes
    dp = [0] * (n + 1)
    dp[0] = 1  
    # Base case: There's one way to arrange
    # 0 nodes (empty tree)
    dp[1] = 1  # Base case: There's one way to 
    # arrange 1 node

    # Fill the dp array using the 
    # Catalan number recurrence relation
    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    # Return the number of unique BSTs for n nodes
    return dp[n]

# Example check
n = 3
print(numTrees(n))  # Output: 5
```

---

### 12. **Matrix Chain Multiplication**

**Example Problem:**  
**LeetCode 312: Burst Balloons**

```python
# Problem: Burst Balloons (Matrix Chain Multiplication pattern)

def maxCoins(nums):
    # Add 1 to both ends of the list for easier calculation (border balloons)
    nums = [1] + nums + [1]
    n = len(nums)
    # DP table where dp[i][j] represents the max coins that can be obtained by bursting balloons between i and j
    dp = [[0] * n for _ in range(n)]

    # Fill the DP table in a bottom-up manner
    for length in range(2, n):
        for left in range(n - length):
            right = left + length
            # Calculate max coins by bursting balloon k last between left and right
            for k in range(left + 1, right):
                dp[left][right] = max(dp[left][right], nums[left] * nums[k] * nums[right] + dp[left][k] + dp[k][right])

    # The result is stored in dp[0][n-1]
    return dp[0][n - 1]

# Example check
nums = [3, 1, 5, 8]
print(maxCoins(nums))  # Output: 167
```

---

### 13. **Count Distinct Ways**

**Example Problem:**  
**LeetCode 91: Decode Ways**

```python
# Problem: Decode Ways

def numDecodings(s):
    # Base case: If the string is empty, there's one way to decode it (doing nothing)
    if not s:
        return 0

    # DP array where dp[i] represents the number of ways to decode s[:i]
    dp = [0] * (len(s) + 1)
    dp[0] = 1  # Base case: There's one way to decode an empty string
    dp[1] = 1 if s[0] !=

 '0' else 0  # Single-character decoding

    # Fill the dp array
    for i in range(2, len(s) + 1):
        # Check if the current character can be decoded as a single digit
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        # Check if the last two characters can be decoded as a valid two-digit number
        if 10 <= int(s[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[len(s)]

# Example check
s = "226"
print(numDecodings(s))  # Output: 3
```

---

### 14. **Number of Ways to Paint a Fence**

**Example Problem:**  
**LeetCode: Paint Fence**

```python
# Problem: Paint Fence

def numWays(n, k):
    if n == 0:
        return 0
    if n == 1:
        return k

    # Base cases
    same, diff = 0, k
    total = same + diff

    # Fill the dp array
    for i in range(2, n + 1):
        same = diff
        diff = total * (k - 1)
        total = same + diff

    return total

# Example check
n = 3
k = 2
print(numWays(n, k))  # Output: 6
```

---

### 15. **Maximal Square**

**Example Problem:**  
**LeetCode 221: Maximal Square**

```python
# Problem: Maximal Square

def maximalSquare(matrix):
    if not matrix:
        return 0

    # Dimensions of the matrix
    m, n = len(matrix), len(matrix[0])
    # DP table where dp[i][j] represents the size of the square with the bottom-right corner at (i, j)
    dp = [[0] * n for _ in range(m)]
    max_side = 0  # Track the maximum side length of the square

    # Fill the dp array
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                # If we're not in the first row or first column, take the min of three neighboring cells
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 1  # If we're at the border, the max square is 1
                max_side = max(max_side, dp[i][j])

    # The result is the area of the maximal square
    return max_side * max_side

# Example check
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
print(maximalSquare(matrix))  # Output: 4 (2x2 square)
```

That covers the rest of the 15 common dynamic programming topics. Let me know if you need any further breakdown or more advanced examples!

Here’s a summary of each dynamic programming topic along with when each topic is useful:

### Extracted Topics and Their Use Cases:

1. **Fibonacci Sequence**
   
   - **Use Case**: Solving problems where the solution depends on the solutions of smaller instances, often with recursive relationships.

2. **Kadane's Algorithm**
   
   - **Use Case**: Optimizing the sum of a contiguous subarray within a one-dimensional numeric array, typically for maximum sum problems.

3. **0/1 Knapsack**
   
   - **Use Case**: Selecting a subset of items with constraints to maximize or minimize total value, where each item can be chosen only once.

4. **Unbounded Knapsack**
   
   - **Use Case**: Maximizing total value by selecting items with constraints, where each item can be chosen multiple times with infinite supply.

5. **Longest Common Subsequence (LCS)**
   
   - **Use Case**: Finding the longest subsequence that appears in the same order in two given sequences.

---

### 1. **Longest Increasing Subsequence (LIS)**

- **Useful for:** Problems where you need to find the longest subsequence in an array where the elements are strictly increasing. Applicable in situations like stock trading to track maximum profit, or arranging items in a certain order.

---

### 2. **Palindromic Subsequence**

- **Useful for:** Problems where you need to identify the longest subsequence that reads the same forward and backward. Common in string processing tasks like DNA sequence analysis or text-based palindrome identification.

---

### 3. **Edit Distance**

- **Useful for:** Comparing two strings and determining the minimum number of operations (insert, delete, replace) needed to convert one string to another. Frequently applied in spell checkers, DNA sequencing, and text comparison applications.

---

### 4. **Subset Sum**

- **Useful for:** Partitioning problems, where you need to decide if a given set of numbers can be divided into two subsets with equal sums. This is important in financial applications and decision-making scenarios with resource allocation.

---

### 5. **String Partition**

- **Useful for:** Problems that require breaking a string into valid words from a given dictionary. It’s commonly used in natural language processing for text segmentation, tokenization, and auto-completion systems.

---

### 6. **Catalan Numbers**

- **Useful for:** Counting the number of unique structures (like binary trees, valid parentheses, etc.) in combinatorial problems. Often encountered in algorithm design, combinatorics, and parsing contexts in computer science.

---

### 7. **Matrix Chain Multiplication**

- **Useful for:** Problems where you need to determine the most efficient way to multiply matrices, by minimizing the number of scalar multiplications. This is applicable in optimization tasks in computer graphics, scientific computing, and numerical simulations.

---

### 8. **Count Distinct Ways**

- **Useful for:** Scenarios where you need to count distinct ways to decode a string or represent a number using specific rules. This concept is commonly used in combinatorics, cryptography, and decoding systems.

---

### 9. **Number of Ways to Paint a Fence**

- **Useful for:** Problems where you need to determine how many distinct ways you can paint a structure (like a fence) subject to certain constraints. Applicable in design optimization, combinatorics, and constraint satisfaction problems.

---

### 10. **Maximal Square**

- **Useful for:** Finding the largest square submatrix of 1s in a binary matrix. It has applications in image processing, pattern recognition, and geographical data analysis to detect clusters or regions.

---

### 14. **DP on Grids**

- **Use case:** This pattern is applied when navigating or optimizing paths within a grid, such as determining the minimum path sum or counting the number of unique paths. It is useful for problems where the solution at each grid cell depends on neighboring cells in different directions (e.g., right, down, diagonal).

---

### 15. **DP on Trees**

- **Use case:** This is useful when working with tree-structured data where decisions made at each node affect its children or ancestors. It applies to problems like computing the maximum sum of nodes or optimizing camera placements for monitoring the tree. Recursive solutions that leverage dynamic programming on subtrees are common.

---

### 16. **DP on Graphs**

- **Use case:** Applied when the problem involves finding optimal paths, longest paths, or other optimized properties in graph-structured data. Useful for traversing graphs and maintaining state for each node or edge based on neighbors or connected components.

---

### 17. **Digit DP**

- **Use case:** Digit DP is applied to problems involving counting or summing over a range of numbers by individually considering their digits. It is particularly useful for problems where constraints are placed on the digits, such as finding numbers with unique digits or counting specific occurrences in large ranges.

---

### 18. **Bitmasking DP**

- **Use case:** This pattern is used for problems that involve combinations or subsets of elements, especially when the number of elements is relatively small. The states of the problem are represented efficiently using bits in an integer, making it useful for problems with up to 20-30 elements and subset inclusion/exclusion decisions.

---

### 19. **Probability DP**

- **Use case:** Applied to problems involving probability calculations, such as determining the probability of an event or the expected value of an outcome. These problems often involve random processes or decision-making under uncertainty, with probabilities depending on previous states.

---

### 20. **State Machine DP**

- **Use case:** Used when a problem can be modeled as a series of states and transitions between them, with a finite number of possible states. This pattern is particularly useful when solving problems that involve making decisions that affect future states, such as optimizing a sequence of actions or maximizing profit over multiple rounds.

---

### LeetCode Problem: **Best Time to Buy and Sell Stock III (LeetCode 123)**

#### Problem Statement:

You are given an array `prices` where `prices[i]` is the price of a given stock on day `i`. You want to maximize your profit by completing **at most two transactions**.

#### Solution (Python code):

```python
def maxProfit(prices):
    if not prices:
        return 0

    n = len(prices)

    # Initialize DP arrays
    dp = [[0] * 3 for _ in range(n)]

    # Iterate over each day
    for k in range(1, 3):  # Maximum two transactions
        max_diff = -prices[0]  # Max difference initialized to buy on the first day
        for i in range(1, n):
            # dp[i][k] represents the max profit on day i with at most k transactions
            dp[i][k] = max(dp[i-1][k], prices[i] + max_diff)
            max_diff = max(max_diff, dp[i-1][k-1] - prices[i])

    return dp[-1][2]  # Return max profit with 2 transactions on the last day
```

#### Explanation:

1. We define a `dp` array where `dp[i][k]` stores the maximum profit on day `i` with at most `k` transactions.
2. For each transaction `k`, we keep track of the maximum difference between `dp[i-1][k-1] - prices[i]`.
3. We iterate through each day `i`, updating the `dp` array based on the maximum profit achieved with the given transaction count.
4. The result is found in `dp[-1][2]`, which gives the maximum profit with at most two transactions by the last day.

---

This solution leverages dynamic programming with a time complexity of \(O(n)\) where \(n\) is the number of days.

##### Date 25th Sep
