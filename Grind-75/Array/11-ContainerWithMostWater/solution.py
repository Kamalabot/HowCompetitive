from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_volume = 0
        left, right = 0, len(height) - 1

        while left != right:  # keep iterating till the end
            # if height[left] is smaller, the only way to increase volume 
            # is to check whether moving left to left + 1 increase the 
            # volume since width is getting smaller.
            if height[left] >= height[right]: 
                # if left is taller use right height
                volume = height[right] * (right - left)
                right -= 1
            else:  # go with left height
                volume = height[left] * (right - left)
                left += 1
            # keep track of max_volume by checking the calculated volume
            max_volume = max(max_volume, volume)
        return max_volume
