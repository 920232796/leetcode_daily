from typing import List 

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        res = sum(nums[0:k])
        cur = res
        for i in range(1, len(nums) - k + 1):
            left = nums[i-1]
            right = nums[i + k - 1]
            cur = cur + right - left
            if left < right:
                # print(i)
                if cur > res:
                    res = cur
            
        
        return float(res) / k



if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAverage([1,12,-5,-6,50,3], 4))