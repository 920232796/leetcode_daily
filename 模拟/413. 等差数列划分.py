
from typing import List 

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0 
        for i in range(len(nums) - 2):
            for j in range(i + 2, len(nums)):
                if self.is_slices(nums[i:j+1]):
                    res += 1
                else :
                    break
        return res 

    def is_slices(self, nums):
        # 判断是否符合情况
        q = -100
        for i in range(len(nums) - 1):
            if q == -100:
                q = nums[i + 1] - nums[i]
            elif nums[i + 1] - nums[i] == q:
                continue 
            else :
                return False
        
        return True

if __name__ == "__main__":
    pass
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4]))