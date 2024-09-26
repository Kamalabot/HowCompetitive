###### Provide the intuition of backtracking problems and use the example of finding all the combination of given array of numbers

### Intuition of Backtracking Problems:

**Backtracking** is a problem-solving technique that builds a solution incrementally, and if a partial solution is invalid or doesn't lead to a complete solution, it "backtracks" by undoing the last step and tries another option. The goal is to explore all possible choices in a systematic manner.

**Key Idea**:

- You make a choice, explore the consequences of that choice recursively, and if it doesn’t lead to a solution, undo the choice (backtrack) and try a different option.
- Backtracking is often used for combinatorial problems, where you need to try all possible ways to solve the problem.

### Example: Finding All Combinations of a Given Array of Numbers

Consider an array `nums = [1, 2, 3]`. We want to find all possible combinations (subsets) of the numbers in this array.

**Steps for Backtracking**:

1. **Base Case**:
   
   - When you've considered all numbers, a valid combination is formed, and you store it.

2. **Recursive Step**:
   
   - At each step, you decide whether to include the current number in the combination or not.
   - You recursively explore both possibilities: include or exclude the number, and backtrack when done.

### Process:

- Start with an empty combination.
- For each number in the array, decide:
  - Include the number in the combination, move to the next number.
  - Exclude the number from the combination, move to the next number.
- When you've processed all the numbers, save the combination and backtrack to explore other combinations.

### Example Walkthrough:

Given `nums = [1, 2, 3]`, the process would look like this:

1. Start with an empty combination `[]`.
2. At `1`:
   - Include `1`: `[1]`
     - At `2`:
       - Include `2`: `[1, 2]`
         - At `3`: 
           - Include `3`: `[1, 2, 3]` (store result)
           - Exclude `3`: `[1, 2]` (store result)
       - Exclude `2`: `[1]`
         - At `3`: 
           - Include `3`: `[1, 3]` (store result)
           - Exclude `3`: `[1]` (store result)
   - Exclude `1`: `[]`
     - At `2`: 
       - Include `2`: `[2]`
         - At `3`: 
           - Include `3`: `[2, 3]` (store result)
           - Exclude `3`: `[2]` (store result)
       - Exclude `2`: `[]`
         - At `3`: 
           - Include `3`: `[3]` (store result)
           - Exclude `3`: `[]` (store result)

### Resulting Combinations:

- `[1, 2, 3]`
- `[1, 2]`
- `[1, 3]`
- `[1]`
- `[2, 3]`
- `[2]`
- `[3]`
- `[]` (empty set)

This backtracking systematically explores all combinations by including/excluding elements and recursing to build the complete solution set.

Here's how the intuition for **backtracking to find all combinations of a given array of numbers** translates into Rust code:

### Rust Code Example:

```rust
fn main() {
    let nums = vec![1, 2, 3];
    let mut result = Vec::new();
    let mut current = Vec::new();

    // Start the backtracking process
    backtrack(&nums, 0, &mut current, &mut result);

    // Print all combinations
    println!("{:?}", result);
}

fn backtrack(nums: &Vec<i32>, start: usize, current: &mut Vec<i32>, result: &mut Vec<Vec<i32>>) {
    // Add the current combination to the result
    result.push(current.clone());

    // Explore all possible combinations starting from 'start'
    for i in start..nums.len() {
        // Include the current number
        current.push(nums[i]);

        // Move to the next number
        backtrack(nums, i + 1, current, result);

        // Backtrack: remove the last number to try a new combination
        current.pop();
    }
}
```

### Step-by-Step Explanation:

1. **Main Function**:
   
   - `nums = vec![1, 2, 3]` is the input array.
   - `result` stores all possible combinations.
   - `current` stores the current combination during the backtracking process.

2. **Backtrack Function**:
   
   - `backtrack` is the recursive function that builds combinations.
   - **Base Case**: There is no explicit base case because we add the current combination to `result` at every step.
   - **Recursive Step**: 
     - Loop through the array starting from the current index `start`.
     - For each number `nums[i]`, it is included in `current` and the recursive function is called with the next index (`i + 1`).
     - After recursion, the number is removed from `current` (backtracking) to explore other possibilities.

3. **Backtracking Logic**:
   
   - **Include the current element** (`current.push(nums[i])`).
   - **Explore further with the next element** (`backtrack(nums, i + 1, current, result)`).
   - **Backtrack by removing the current element** (`current.pop()`) to try different combinations.

### Output:

The code will print all combinations (subsets) of the array `[1, 2, 3]`:

```plaintext
[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
```

### Intuition Recap:

- For each number, you decide whether to **include** it in the current combination or **exclude** it.
- After making a decision (include or exclude), you **recursively** explore the next numbers.
- Once you've explored one path, you **backtrack** by undoing the last decision (removing the number) and trying another path.

This is a clear example of how backtracking systematically explores all possibilities, while using recursion and state undoing (backtracking) to achieve the result.

Yes, exactly! Here's a breakdown of the **backtracking process** in terms of the two lists you're referring to:

1. **Current List**: 
   
   - This list holds the current subset or combination being built as you move through the elements of the input list.
   - You include elements in this list, move forward, and continue adding more elements.
   - Once a full valid subset is formed, you add this "current" list to the **global result list**.

2. **Global Result List**:
   
   - This is the list that holds all the possible subsets/combinations. 
   - Every time you reach a point where a valid subset is formed (which could be at every level in the recursion), you append a copy of the **current list** to this global result list.

### Key Steps in the Process:

- **Include** an element in the current list, move forward to the next element.
- **Recurse** deeper with this updated current list until you've considered all elements.
- Once you've explored all possibilities at that level, you **backtrack** by removing the last added element from the current list and explore the alternative of not including it (i.e., excluding it).
- Repeat this process to generate all possible combinations.

### Example Flow for `[1, 2, 3]`:

- Start with an empty `current` list (`[]`).
1. **Include 1**:
   - `current = [1]`, recurse.
2. **Include 2**:
   - `current = [1, 2]`, recurse.
3. **Include 3**:
   - `current = [1, 2, 3]`, recurse (end of input list).
   - Append `[1, 2, 3]` to the global result.
   - **Backtrack**: Remove 3 → `current = [1, 2]`.
4. **Exclude 3**:
   - `current = [1, 2]`, append to result.
   - **Backtrack**: Remove 2 → `current = [1]`.
5. **Include 3**:
   - `current = [1, 3]`, recurse.
   - Append `[1, 3]` to result.
   - **Backtrack**: Remove 3 → `current = [1]`.
   - **Backtrack**: Remove 1 → `current = []`.
6. **Continue the process** with other elements, eventually generating all subsets.

This ensures all possible combinations (subsets) of the array are explored!

###### whether a element is pushed into the result depends on whether for loop executes and that depends on whether there are elements

Exactly! The process of pushing an element into the result is determined by the execution of the **for loop**, which controls the decision of including or excluding each element. Whether the loop continues depends on the availability of elements in the array.

### Detailed Breakdown:

1. **For Loop Execution**:
   
   - At each recursive level, the for loop iterates over the remaining elements starting from the current index.
   - For each element, the loop makes a decision:
     - **Include** the current element in the combination.
     - Recursively process the next elements.

2. **Recursion**:
   
   - After including an element, the recursive call processes the next index (moving forward).
   - If the loop still has elements to process, it continues including the next element.
   - If there are no more elements to process (i.e., end of the array), the recursion stops, and the current combination is pushed into the result.

3. **Backtracking**:
   
   - After the loop finishes, it **backtracks** by undoing the last inclusion (removing the element) and tries the alternative: **excluding** that element.

4. **Element Pushed to Result**:
   
   - Every time the recursion reaches a new level (with a complete or partial combination in the current list), that combination is pushed into the global result list.
   - This happens both when elements are included and when excluded.

### Summary:

- The **for loop** iterates over elements, ensuring that each element has the chance to be included or excluded.
- The recursive calls move deeper into the element list as long as there are unprocessed elements.
- Once all possibilities for a combination are exhausted, the current combination is added to the result list.

Backtracking on Stock market pricing

### Backtracking in Stock Market Problems

Backtracking can be used in stock market problems where you need to explore all possible transactions to maximize profit or to find the best trading strategy under certain constraints. One common problem involves determining the best time to buy and sell stocks given a series of prices.

### Example: Finding Maximum Profit with Stock Transactions

**Problem Statement**: Given an array of stock prices where `prices[i]` is the price of a given stock on the `i-th` day, determine the maximum profit you can achieve by buying and selling the stock. You can complete at most one transaction (i.e., buy one and sell one share of the stock).

### Backtracking Approach:

1. **Variables**:
   
   - You need to track the current minimum price seen so far and the maximum profit you can achieve.

2. **Backtracking Logic**:
   
   - Iterate through each price in the list.
   - For each price, decide whether to buy (update the minimum price) or sell (calculate profit based on the current price and the minimum price).
   - Use recursion to explore the profits you can achieve as you progress through the list.
   - Backtrack to explore different combinations of buying and selling.

### Example Walkthrough:

Given `prices = [7, 1, 5, 3, 6, 4]`:

1. **Initialization**:
   
   - Start with an infinite minimum price (initially the maximum possible).
   - Initialize maximum profit to zero.

2. **Iterate through Prices**:
   
   - Day 0: Price = 7 → Minimum price = 7
   - Day 1: Price = 1 → Update minimum price = 1
   - Day 2: Price = 5 → Calculate profit = 5 - 1 = 4 (update maximum profit = 4)
   - Day 3: Price = 3 → Profit = 3 - 1 = 2 (no update to maximum profit)
   - Day 4: Price = 6 → Profit = 6 - 1 = 5 (update maximum profit = 5)
   - Day 5: Price = 4 → Profit = 4 - 1 = 3 (no update to maximum profit)

### Result:

- The maximum profit achievable from this sequence of prices is **5**, by buying at price `1` and selling at price `6`.

### Summary:

In this stock market example, backtracking helps explore all potential buy-sell combinations while optimizing for maximum profit by keeping track of the minimum price and calculating profits dynamically. It ensures all options are considered to find the best strategy.

Here’s a basic implementation of the **backtracking approach** to find the maximum profit in stock trading, where you are allowed to complete at most one transaction:

### Code in Rust:

```rust
fn max_profit(prices: Vec<i32>) -> i32 {
    // Initialize variables to store the minimum price and maximum profit
    let mut min_price = i32::MAX;
    let mut max_profit = 0;

    // Iterate through the prices
    for price in prices {
        // Update the minimum price if the current price is lower
        if price < min_price {
            min_price = price;
        }

        // Calculate the profit if we sell at the current price
        let profit = price - min_price;

        // Update the maximum profit if the calculated profit is higher
        if profit > max_profit {
            max_profit = profit;
        }
    }

    // Return the maximum profit
    max_profit
}

fn main() {
    // Example stock prices
    let prices = vec![7, 1, 5, 3, 6, 4];

    // Call the function and print the result
    let result = max_profit(prices);
    println!("Maximum Profit: {}", result);
}
```

### Explanation:

1. **Variables**:
   
   - `min_price`: Tracks the lowest stock price encountered so far (initialized to a very high number, `i32::MAX`).
   - `max_profit`: Stores the highest profit calculated from buying at the minimum price and selling at the current price.

2. **For Loop**:
   
   - For each price in the list:
     - Update the `min_price` if the current price is lower than the previously recorded minimum.
     - Calculate the potential profit by subtracting `min_price` from the current price.
     - Update `max_profit` if this newly calculated profit is greater than the previously recorded maximum profit.

3. **Result**:
   
   - The function returns the maximum profit that can be achieved by completing one buy-sell transaction.

### Example Execution:

- For the input `prices = [7, 1, 5, 3, 6, 4]`, the maximum profit is **5**, as explained earlier (buy at price 1 and sell at price 6).

###### Above problem solved with recursion

To implement the stock market problem using **recursion** instead of using a loop for backtracking, we can adopt a different approach. Here, we recursively calculate the maximum profit by traversing the array of prices, updating the minimum price, and checking for potential profits at each step.

### Recursive Approach:

We break down the problem as follows:

1. **Base Case**: If we've reached the end of the price list, return 0 (no more profit to be made).
2. **Recursive Case**: At each price:
   - Compare it with the current minimum price.
   - Recursively move to the next day's price and check the profit if we sell at the current price.

Here’s a recursive solution for finding the maximum profit:

### Recursive Rust Code:

```rust
fn max_profit_recursive(prices: &[i32], index: usize, min_price: i32, max_profit: i32) -> i32 {
    // Base case: if we have processed all days, return the max profit found
    if index == prices.len() {
        return max_profit;
    }

    // Calculate the minimum price so far
    let min_price = min_price.min(prices[index]);

    // Calculate the potential profit if selling on this day
    let profit = prices[index] - min_price;

    // Update the maximum profit
    let max_profit = max_profit.max(profit);

    // Recursively check the next day
    max_profit_recursive(prices, index + 1, min_price, max_profit)
}

fn main() {
    let prices = vec![7, 1, 5, 3, 6, 4];

    // Start recursion from the first day (index 0) with initial max_profit = 0 and min_price = MAX
    let result = max_profit_recursive(&prices, 0, i32::MAX, 0);

    println!("Maximum Profit: {}", result);
}
```

### How This Recursive Approach Works:

1. **Parameters**:
   
   - `prices`: The array of stock prices.
   - `index`: The current day (starting from day 0).
   - `min_price`: The minimum stock price encountered so far.
   - `max_profit`: The maximum profit encountered so far.

2. **Base Case**:
   
   - If `index` equals the length of the `prices` array, it means we’ve processed all prices, and we return the current `max_profit`.

3. **Recursive Case**:
   
   - For the current price at `index`, we update the minimum price (`min_price`).
   - Calculate the profit for the current day: `prices[index] - min_price`.
   - Update `max_profit` if the current profit is greater than the previous maximum.
   - Recursively call the function for the next day's price (`index + 1`).

### Example Execution Flow:

For `prices = [7, 1, 5, 3, 6, 4]`:

- Start at index `0` with `min_price = i32::MAX` and `max_profit = 0`.
- Recursively process each price, updating `min_price` and `max_profit` as you move through the array.
- Finally, the recursive function will return the maximum profit possible: **5**.

### Intuition Behind Recursion:

- At each recursive call, we either:
  - Update the `min_price` if we find a lower price.
  - Calculate the potential profit and update `max_profit` if it's higher.
- We make recursive calls to explore the remaining prices, ensuring we cover all buy/sell combinations step by step.

The **recursive** and **backtracking** methods for finding combinations, subsets, and permutations are conceptually similar but differ in how they handle exploration and decision-making:

### 1. **Recursive Approach**:

- **Purpose**: Directly explores all possibilities.
- **Nature**: Calls the function recursively for each branch, without much pruning of invalid or unnecessary paths.
- **Depth**: May explore all branches fully (including some invalid ones), leading to higher time complexity in certain cases.

#### Example (Recursive Subset):

```python
def subsets_recursive(nums):
    result = []

    def helper(i, current):
        if i == len(nums):
            result.append(current)
            return
        helper(i + 1, current)           # Exclude nums[i]
        helper(i + 1, current + [nums[i]]) # Include nums[i]

    helper(0, [])
    return result
```

### 2. **Backtracking Approach**:

- **Purpose**: Focuses on efficient exploration by **pruning unnecessary paths** early. It "backtracks" when a decision leads to an invalid or unwanted result.
- **Nature**: Backtracking is a refined form of recursion. It tries a path, and if it leads to a dead end or a non-optimal solution, it **reverts (backtracks)** to try a different path.
- **Depth**: It avoids fully exploring paths that are invalid earlier, making it generally more efficient in problems with constraints.

#### Example (Backtracking Subset):

```python
def subsets_backtracking(nums):
    result = []

    def backtrack(start, current):
        result.append(list(current))  # Include the current subset
        for i in range(start, len(nums)):
            current.append(nums[i])   # Choose the current element
            backtrack(i + 1, current) # Explore further with the chosen element
            current.pop()             # Backtrack (undo the choice)

    backtrack(0, [])
    return result
```

### **Key Differences**:

1. **Backtracking Prunes Paths**: Backtracking often terminates recursive calls early by rejecting invalid or suboptimal solutions. In contrast, pure recursion may explore all branches without pruning.

2. **Efficiency**: Backtracking is typically more efficient than brute-force recursion, especially in constrained problems, because it doesn't explore unnecessary paths.

3. **State Reversal**: Backtracking explicitly undoes a choice (using techniques like `.pop()`), while recursion might not involve state reversal but rather branches off completely.

### Use Case:

- **Backtracking** is often used in problems where constraints are important, like the **N-Queens problem** or **solving Sudoku**.
- **Recursion** is simpler and more direct, especially when you need to explore all possibilities without additional constraints (e.g., generating subsets or combinations without constraints).
