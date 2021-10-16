

from typing import List 

## 要点： 每次都找最远距离

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_len = 0
        res = 0
        start = 0
        while max_len < len(nums) - 1:
            
            for i in range(start, max_len+1):
                if (i + nums[i]) > max_len:
                    max_len = i + nums[i]
                    start = i
            
            res += 1 
            
        return res 

if __name__ == "__main__":
    s = Solution()
    print(s.jump([0]))


