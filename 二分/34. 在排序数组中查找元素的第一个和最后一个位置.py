from typing import List 


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pass 
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                left = middle
                while left > -1:
                    if nums[left] != target :
                        res.append(left+1)
                        break
                    if left == 0:
                        res.append(left)
                    left -= 1
                right = middle
                while right < len(nums):
                    if nums[right] != target :
                        res.append(right - 1)
                        break
                    if right == len(nums) - 1:
                        res.append(right)
                    right += 1
                return res 
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1

        return [-1, -1]

s = Solution()

print(s.searchRange([2, 2], 2))