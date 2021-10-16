from typing import List 


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pass

        left = 0
        right = left + 1
        while right < len(nums):
            if nums[right] == nums[left] :
                right = right + 1
                continue
            left = left + 1
            nums[left] = nums[right]
            right = right + 1
        # print(nums[:5])
        return left + 1


if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))