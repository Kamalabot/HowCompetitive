from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # start by sorting, so same numbers come close
        # negative nums come to beginning
        output_list = []  # create a list store
        # [-1,0,1,2,-1,-4]  -> [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums)):  # enumerate on the numbers in list
            # every loop the elem in earlier index will be left out # 
            if nums[i] > 0:  # any number above 0 should terminate loop
                break  # exits the loop as there are no negative nums,
                # 0 sum cannot be achieved
            if i > 0 and nums[i] == nums[i - 1]:  # if adj nums are same
                continue  # moves to the next iteration to avoid duplicates
            
            target = -nums[i]  # make -value at curr idx as target
            left, right = i + 1, len(nums) - 1  # 2 indices, left and right most
            while left < right:  # create a while loop
                total = nums[left] + nums[right] # get total of extreme ends
                if target == total:
                    # when the val at nums[i] is added to total, it will be 0
                    output_list.append([nums[i], nums[left], nums[right]])
                    left += 1  # increment the left idx by 1
                    while left < right and nums[left] == nums[left - 1]:
                        # move left idx by one to right if duplicates found
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # move right idx by one to left if duplicates found 
                        right -= 1
                elif target < total:  # if tgt is less than total
                    right -= 1  # move right idx by 1 to left
                else:  # tgt is greater then move left idx by 1 to right  
                    left += 1

        return output_list

