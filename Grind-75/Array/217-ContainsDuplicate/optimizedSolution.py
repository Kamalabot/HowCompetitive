from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        memo = set()  # create a set
        for number in nums: # enumerate nums
            if number in memo:
                # check if elem in set
                return True
            else:
                memo.add(number)
                # if not add in set
        # no repetition then return False
        return False
