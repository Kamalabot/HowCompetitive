from typing import List

# [1,2,3,4] and [-1,1,0,-3,3]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_poduct, output_list = 1, []
        # prefixPdt and output store is created
        for number in nums:  # elems are enumerated
            output_list.append(prefix_poduct)
            # keep prefix product first in store
            prefix_poduct *= number
            # updt the prefix product with elems prdt
        # print(output_list)  # [1, 1, 2, 6]
        suffix_poduct = 1  # create suffixPdt
        for i in range(len(nums) - 1, -1, -1):  # enumerate elems backwards
            output_list[i] *= suffix_poduct
            # output list element is updt with suffix pdt
            suffix_poduct *= nums[i]

        return output_list


x = [1, 2, 3, 4]

sln = Solution()
print(sln.productExceptSelf(x))