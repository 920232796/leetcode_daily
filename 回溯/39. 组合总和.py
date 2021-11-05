from typing import List 


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pass
        self.candidates = sorted(candidates)
        self.target = target
        self.res = []

        self.solve([], 0)

        return self.res 
        
    
    def solve(self, tmp, tmp_sum):
        pass
        for i in self.candidates:
            if tmp_sum + i > self.target:
                return 
            elif tmp_sum + i == self.target:
                if sorted(tmp + [i]) not in self.res:
                    self.res.append(tmp + [i])
                return 
            else :
                self.solve(tmp + [i], tmp_sum + i)
        


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))