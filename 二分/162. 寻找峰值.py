
from typing import List 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        pass
        total = len(nums)
        if total == 1:
            return 0
        l = 0
        r = total - 1

        while l < r:
            middle = (l + r) // 2
            if nums[middle] > nums[middle + 1]:
                r = middle 
            # elif nums[middle] < nums[middle + 1] :
            #     l = middle + 1
            else :
                l = middle + 1
        return l

nums = [4, 3, 3, 3, 3, 3]
s = Solution()
print(s.findPeakElement(nums))