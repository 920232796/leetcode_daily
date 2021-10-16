from typing import List 
import os 

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        pass
        self.G = [[0 for i in range(n)] for j in range(n)]

        cirlces = n // 2 + 1

        x, y = 0, 0
        self.G[0][0] = 1
        while n > 1:
            x, y = self.one_circle(x, y, n)
            n = n - 2
            if n >= 1:
                self.G[x][y] = self.G[x][y - 1] + 1

        return self.G
    def one_circle(self, x, y, n):
        
        # 先往左走 n - 1次
        for i in range(1, n):
            self.G[x][y + i] = self.G[x][y] + i
        
        for i in range(1, n):
            self.G[x + i][y + n-1] = self.G[x][y + n-1] + i

        for i in range(1, n):
            self.G[x + (n - 1)][y + n - 1 - i] = self.G[x + (n - 1)][y + (n - 1)] + i

        for i in range(1, n - 1):
            self.G[x + n - 1 - i][y] = self.G[x + (n - 1)][y] + i 

        return x + 1, y + 1

if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))
