

from typing import List 


# ## 暴力求解
# class Solution:
#     def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
#         pass 
#         left = 0
#         total = len(nums)
#         res = []
#         while left <= (total - k):
#             sorted_res = sorted(nums[left: left + k])
#             if k % 2 == 0:
#                 # 偶数
#                 res.append((sorted_res[- 1 + k//2] + sorted_res[k//2]) / 2)
#             else :                
#                 res.append(sorted_res[(k-1)//2])
#             left += 1
#         return res

## 优化求解
class Solution:

    def insert_pop(self, n1, n2):
        pass
        n1_index = self.binary_find(n1)
        self.window_nums.pop(n1_index)
        n2_index = self.binary_insert(n2)
        self.window_nums.insert(n2_index, n2)
    
    def binary_find(self, x):
        left = 0
        right = len(self.window_nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if self.window_nums[middle] == x:
                return middle
            elif self.window_nums[middle] > x:
                right = middle - 1
            else :
                left = middle + 1
    
    def binary_insert(self, x):
        # 二分插入 求插入的index位置
        pass 
        left = 0
        right = len(self.window_nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if self.window_nums[middle] == x:
                return middle
            elif self.window_nums[middle] > x:
                right = middle - 1
            else :
                left = middle + 1
        return left 
        
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        pass 
        left = 0
        total = len(nums)
        res = []
        self.window_nums = sorted(nums[:k])
        while left <= (total - k):
            if k % 2 == 0:
                # 偶数
                res.append((self.window_nums[- 1 + k//2] + self.window_nums[k//2]) / 2)
            else :                
                res.append(self.window_nums[(k-1)//2])

            # 在这进行插入移出操作。
            if left != total - k:
                self.insert_pop(nums[left], nums[left+k])
            left += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
    # s.window_nums = [0, 1, 3, 4]

    # print(s.binary_insert(4))
    # 