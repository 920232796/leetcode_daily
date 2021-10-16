from typing import List 


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_num = -100
        while left < right:
            v = (right - left) * min(height[left], height[right])
            if v > max_num:
                max_num = v 
            if height[left] < height[right]:
                left = left + 1
            else :
                right = right - 1
        
        return max_num


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))


