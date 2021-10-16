
from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        j = -1
        for i in range(len(nums) - 2, -1, -1):
            
            if nums[i] >= nums[j]:
                j = j - 1
            
            else :
                ## 找到可以交换的了
                # 找一个尽量小的！
                for j in range(len(nums) - 1, i, -1):
                
                    if nums[j] > nums[i]:
                        if nums[k] < nums[i]:
                            k = j 
                        else :
                            if nums[j] < nums[k]:
                                k = j 
                    
                nums[k], nums[i] = nums[i], nums[k]
                
                i = i + 1
                j = len(nums) - 1
                while i < j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
                    j = j - 1
                    

                return nums
            # if nums[k] > nums[i]:
            #     nums[k], nums[i] = nums[i], nums[k]
            #     
            #     return nums

            # k = i 

        
        nums.sort()

        return nums

if __name__ == "__main__":
    s = Solution() ##2  3  1
    print(s.nextPermutation([1, 5, 1]))
    # a = [2, 3, 1, 2, 3, 2]
    # print(a[2:4])
    # a = a[0:2] + sorted(a[2:6])
    # print(a)