from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # start by sorting
        output_list = []  # create a list store

        for i in range(len(nums)):  # enumerate on the numbers in list
            if nums[i] > 0:  # any number above 0 should terminate loop 
                break  # exits the loop
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # moves to the next iteration to avoid duplicates

            target = -nums[i]  # make -value at curr idx as target
            left, right = i + 1, len(nums) - 1  # 2 indices, left and right
            while left < right:  # create a while loop
                total = nums[left] + nums[right] # get total of extreme ends
                if target == total:
                    # when the val at nums[i] is added to total, it will be 0
                    output_list.append([nums[i], nums[left], nums[right]])
                    left += 1  # increment the left idx by 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                elif target < total:
                    right -= 1
                else:
                    left += 1

        return output_list

            