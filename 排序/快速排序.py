from typing import List 

class Solution:
    def quick_sort(self, nums, start, end):
        if start >= end :
            return 
        
        pivot = nums[start]
        index = start + 1
        for i in range(start + 1, end + 1):
            if nums[i] < pivot:
                #需要交换
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        nums[start], nums[index - 1] = nums[index - 1], nums[start]

        self.quick_sort(nums, start, index - 1)
        self.quick_sort(nums, index, end)

        return nums

s = Solution()
n = s.quick_sort([3, 5, 6, 2, 1, 4, 7], 0, 6)

print(n)
# print(s.judge(30, 34))