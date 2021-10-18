
from typing import List 


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        pass
        number = 0
        for left in range(len(nums) - 2):
            right = left + 1
            q = nums[right] - nums[left]
            right += 1
            while right < len(nums):
                if nums[right] - nums[right - 1] == q:
                    number += 1
                    right += 1
                else :
                    break 
        
        return number
        


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfArithmeticSlices([1,2,3,4]))
