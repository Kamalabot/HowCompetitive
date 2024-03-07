class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        memo = {}  # declare memo, don't populate
        for i, j in enumerate(nums):  # enumerate list along with index
            number_to_find = target - j  # get the complement of val at curr ind
            try:
                return [memo[j], i]  # consider j as complement, and then extract its opp index 
            except KeyError:
                memo[number_to_find] = i  # make the complement as key and attach index as value
