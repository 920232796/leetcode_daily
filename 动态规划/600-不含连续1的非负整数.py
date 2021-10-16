
from typing import List

## 110  0--  0-
## 101 000 001 010            
class Solution:

    def __init__(self) -> None:
        self.f = [[0, 0], [1, 2]]
        
        for i in range(1, 50):
            self.f.append([0, 0])
            self.f[i + 1][0] = self.f[i][1]
            self.f[i + 1][1] = self.f[i][0] + self.f[i][1]
        print(self.f[:4])

    def findIntegers(self, n: int) -> int:
        ## 110  -> 10 01 0 1
        lens = self.getLen(n)
        
        prev = 0
        res = 0
        for i in range(lens, -1, -1):
            cur = (n >> i) & 1 ## 求当前位是0还是1
            if cur == 1:
                res += self.f[i+1][0]
                print(f"i is {i}, f is {self.f[i+1][0]}")
            if cur == 1 and prev == 1:
                break 
            prev = cur
            if i == 0:
                res += 1
        
        return res 

    def getLen(self, n):
        for i in range(32, -1, -1):
            # print(i)
            if n >> i & 1 == 1 :
                return i
    
        return 0

if __name__ == "__main__":
    n = 6 ## 6 -> 110  1: 000 001 010 1: 00, 01     :101,100
    s = Solution()
    print(s.findIntegers(n))

    # print(getLen(6))

  
