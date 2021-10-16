from typing import List 


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_len = 0
        for i, j in enumerate(nums):
            if i <= max_len:
                if i + j > max_len:
                    max_len = i + j 
            else :
                break
        return max_len >= len(nums) - 1


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
