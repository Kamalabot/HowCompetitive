from typing import List


def combine(nums: List[int], k: int) -> List[List[int]]:
    result = []

    # Helper function for recursive backtracking
    def backtrack(start: int, path: List[int]):
        # Base case: when we have a combination of length k
        if len(path) == k:
            result.append(path[:])
            return

        # Iterate over the remaining elements
        for i in range(start, len(nums)):
            # Choose the current element
            path.append(nums[i])
            # Recur to select the next element, starting from i+1 to avoid reusing the same element
            backtrack(i + 1, path)
            # Backtrack by removing the last element before the next iteration
            path.pop()

    # Start the backtracking process
    backtrack(0, [])
    return result


your_list = [1, 2, 3]
print(combine(your_list, 2))
