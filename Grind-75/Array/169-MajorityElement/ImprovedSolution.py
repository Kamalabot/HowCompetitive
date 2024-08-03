from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        memo = {}
        threshold = len(nums) // 2  # majority needs to be more than quotient
        for number in nums:  # enumerate the list
            try:
                memo[number] += 1  # if able to update the count, do that
            except KeyError:
                memo[number] = 1  # raised error, then create a key & value of 1
                
            if memo[number] > threshold:  # if a count crosses threshold then 
                    return number  # return the number
