from typing import List 


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        pass 
        self.candidates = sorted(candidates)
        self.target = target
        self.res = []

        self.solve(0, [], 0)

        return self.res 
        
    def solve(self, k, tmp, tmp_sum):
        pass
        if k >= len(self.candidates):
            return
        for j in range(k, len(self.candidates)):
            if j > k and self.candidates[j] == self.candidates[j - 1]:
                continue
            i = self.candidates[j]
            if tmp_sum + i > self.target:
                return 
            elif tmp_sum + i == self.target:
                self.res.append(tmp + [i])
                return 
            else :
                self.solve(j + 1, tmp + [i], tmp_sum + i)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10,1,2,7,6,1,5], 8))