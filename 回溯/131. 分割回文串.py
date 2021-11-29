

from typing import List 

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        pass 
        if len(s) == 0:
            return []
        if len(s) == 1:
            return [[s]]
        self.s = s 
        self.res = []
        self.record = [[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        self.solve(0, [])

        return self.res 

    def solve(self, i, cur_s_list):
        if i == len(self.s):
            self.res.append(cur_s_list)
            return
        
        for k in range(i+1, len(self.s)+1):
            if self.record[i][k-1] == 1:
                ## 不是回文
                continue
            if self.record[i][k-1] == 2 or self.is_hui(i, k):
                # 左侧是回文 才会继续
                new_list = cur_s_list + [self.s[i:k]]
            
                self.solve(k, new_list)

    def is_hui(self, i, j) -> bool:
       
        while i < j:
            if self.s[i] == self.s[j-1]:
                i += 1
                j -= 1
                continue
            else :
                self.record[i][j-1] = 1
                return False
       
        self.record[i][j-1] = 2
        return True 


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    # print(s.partition("bb"))
    # print(s.is_hui("aba"))