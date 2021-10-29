from typing import List 

## 直接求恰好k个不同整数的子数组，并不好求，因为 考虑 滑窗[low, high] ，先右移high，
# 如果满足，则一直右移high，如果不满足，则需要右移low，那么这时候 high 仍然要回来，重新进行右移
# 这样就导致了，计算复杂度非常高，超出时间限制了。

# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         pass
#         total = len(nums)
#         # 计数    
#         res = []
#         # 窗口大小至少为k
#         left = 0
#         while left <= total - k:
#             if_nums = [0 for i in range(len(nums))]
#             right = left + k - 1
#             for i in range(left, right):
               
#                 if if_nums[nums[i]-1] == 0:
#                     if_nums[nums[i]-1] = 1
                

#             while right < total:

#                 if if_nums[nums[right]-1] == 0:
#                     if_nums[nums[right]-1] = 1

#                 if sum(if_nums) == k:
#                     res.append(nums[left:right+1])
#                 elif sum(if_nums) > k:
#                     break 
                
#                 right = right + 1
                

#             left = left + 1
#         return len(res) 

class Solution:

    def solve(self, k):
        pass
        total = len(self.nums)
        # 计数    
        res = 0
        # 窗口大小至少为k
        left = 0
        right = left
        nums_dis = 1
        if_nums = [0 for i in range(total)]
        if_nums[self.nums[0] - 1] = 1
        compute_nums = [0 for i in range(total)]
        compute_nums[self.nums[0] - 1] = 1

        while right < total and left <= right:

            if nums_dis <= k:
                res += (right - left + 1)

                right = right + 1
                if right < total :
                    tmp = self.nums[right] - 1
                    if compute_nums[tmp] == 0:
                        nums_dis += 1
                    compute_nums[tmp] += 1
                    
                else :
                    break 
                
            else :
                # low 移动
                # print(left, right)
                temp = self.nums[left] - 1
                compute_nums[temp] -= 1
                if compute_nums[temp] == 0:
                   nums_dis -= 1

                left += 1

        # print(res)
        return res

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
       self.nums = nums 
       
       res_k = self.solve(k)
       res_k_1 = self.solve(k-1)

    #    print(res_k)
    #    print(res_k_1)
       return res_k - res_k_1
                

if __name__ == "__main__":
    s = Solution()
    # print(s.subarraysWithKDistinct([1,2,1,2,3], 2))
    print(s.subarraysWithKDistinct([1, 2], 1))

