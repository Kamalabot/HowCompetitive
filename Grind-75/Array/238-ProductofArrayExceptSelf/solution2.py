from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_list = [1] * len(nums)  # start by output list of 1s
        prefix_poduct = suffix_poduct = 1  # create suf / pref pdt
        for index, number in enumerate(nums):
            # number at idx is mul by 1
            output_list[index] *= prefix_poduct
            # update output list with prefix
            prefix_poduct *= number
            # number at reverse idx is mul by 1
            output_list[-1-index] *= suffix_poduct
            # do suffix product for other elems
            suffix_poduct *= nums[-1-index]
        # learning the output transformation is a challenge
        return output_list
