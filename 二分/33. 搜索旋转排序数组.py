
from typing import List 


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0 
            else :
                return -1 
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
        # 找到旋转位置 left 
        self.k = left 
        # print(f"k is {self.k}")
        left_true = left 
        right_true = left_true - 1
        left_fake = self.convert_fake(left_true)
        right_fake = self.convert_fake(right_true)

        while left_fake <= right_fake:
            middle = (left_fake + right_fake) // 2
            middle_true = self.convert_true(middle)
            if nums[middle_true] == target:
                return middle_true 
            if nums[middle_true] > target :
                right_fake = middle - 1
            elif nums[middle_true] < target:
                left_fake = middle + 1

        return -1
    
    def convert_true(self, pos):
        return (pos + self.k) % self.len
    
    def convert_fake(self, pos):
        return (pos + self.len - self.k) % self.len
    
    def binary_search(self, nums, target):
        right = len(nums) - 1
        left = 0
        while left <= right:

            middle = (left + right) // 2
            if target == nums[middle]:
                return middle 
            
            if nums[middle] > target:
                right = middle - 1
            
            elif nums[middle] < target:
                left = middle + 1
            

        return -1


if __name__ == "__main__":
    s = Solution()
    nums = [4, 5, 6, 7, 8, 9, 0, 1, 2, 3]
    # nums = [3, 1]
    # nums = [4, 5, 0, 1, 2, 3]
    # nums = [0, 1, 3, 4, 5, 6, 7]
    target = 3
    # target = 0
    print(s.search(nums, target))