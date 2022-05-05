from typing import List 

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        self.quick_sort(nums, 0, len(nums)-1)
        res = ""
        for num in nums:
            res += str(num)
        
        if res[0] == "0":
            return "0"
        return res 

       
    def quick_sort(self, nums, start, end):
        if start >= end :
            return 
        
        pivot = nums[start]
        index = start + 1
        for i in range(start + 1, end + 1):
            if str(nums[i]) + str(pivot) > str(pivot) + str(nums[i]):
                #需要交换
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
        nums[start], nums[index - 1] = nums[index - 1], nums[start]

        self.quick_sort(nums, start, index - 1)
        self.quick_sort(nums, index, end)

s = Solution()
# nums = [3, 30, 34, 5, 9]
nums = [34323,3432]
print(s.largestNumber(nums))
# n = s.quick_sort([3, 5, 6, 2, 1, 4, 7], 0, 6)

# print(n)
# print(s.judge(30, 34))