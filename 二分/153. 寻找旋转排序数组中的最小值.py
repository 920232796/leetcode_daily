
from typing import List 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass 
        self.len = len(nums)
        right = len(nums) - 1
        left = 0 
        middle = 0
        while left < right:
            middle = (left + right) // 2
            if nums[middle] > nums[right]:
                left = middle + 1
            else :
                right = middle
        return nums[left]


if __name__ == "__main__":
    s = Solution()
    nums = [3, 4, 5, 1, 2]
    print(s.findMin(nums))