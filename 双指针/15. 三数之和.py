from typing import List 


## 超出时间限制
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         pass
#         if len(nums) < 3:
#             return []
#         res = []
#         left = 0
#         middle = 1
#         right = 2
#         while left < len(nums) - 2:
#             while middle < len(nums) - 1:
#                 while right < len(nums):
#                     if nums[left] + nums[middle] + nums[right] == 0:
#                         if sorted([nums[left], nums[middle], nums[right]]) not in res:
                            
#                             res.append(sorted([nums[left], nums[middle], nums[right]]))
#                         break 
#                     right += 1
#                 middle += 1
#                 right = middle + 1
#             left += 1
#             middle = left + 1
#             right = middle + 1

#         return res 

# 超出时间限制
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
        nums = sorted(nums)
        if len(nums) < 3:
            return []
        res = []
        
        left = 0
        middle = 1
        right = 2
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                return res 
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                sum_mr = nums[middle] + nums[right]
                
                if -nums[left] == sum_mr:
                    r = sorted([nums[middle], nums[left], nums[right]])
                    if r not in res:
                        res.append(r)
                    middle += 1
                    right -= 1
                elif sum_mr < -nums[left]:

                    middle += 1
                else :
                    right -= 1

                

        return res 





if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))

