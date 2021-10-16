

from typing import List 

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pass 

        left = 0
        right = left
        while right < len(nums):
            if nums[right] == val:
                right += 1
            else :
                nums[left] = nums[right]
                right += 1
                left += 1
        # print(nums[:left])
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.removeElement([3, 2, 2, 3], 3))