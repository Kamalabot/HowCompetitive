class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):  # enumerate on the length of the list
            number_to_find = target - nums[i]  # search of the complement number
            for j in range(i + 1, len(nums)):  # Leave the current index and enumerate
                if nums[j] == number_to_find:  # if any of the index contains complement
                    return [i, j]  # return i, j indices
