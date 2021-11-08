from typing import List 


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        pass
        
        self.nums = sorted(nums)
        self.res = [[]]

        self.solve(0, [])

        return self.res  

    def solve(self, k, tmp):
        pass
        if k >= len(self.nums):
            return
        for j in range(k, len(self.nums)):
            if j > k and self.nums[j] == self.nums[j - 1]:
                continue
            i = self.nums[j]
            self.res.append(tmp + [i])
            self.solve(j + 1, tmp + [i])




if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1,2,2]))