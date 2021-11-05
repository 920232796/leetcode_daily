from typing import List 


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == "":
            return []
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        self.res = []
        self.all_alpha = []
        for d in digits:
            self.all_alpha.append(KEY[d])
        
        
        if len(self.all_alpha) == 1:
            return self.all_alpha[0]
        
        self.solve("", 0)
        return self.res

    def solve(self, tmp, j):
        if j == len(self.all_alpha):
            self.res.append(tmp)
            return 
        
        alpha = self.all_alpha[j]
        for a in alpha:
            tmp1 = tmp + a
            self.solve(tmp1, j + 1)




if __name__ == "__main__":
    s = Solution()
    print(s.letterCombinations("23"))