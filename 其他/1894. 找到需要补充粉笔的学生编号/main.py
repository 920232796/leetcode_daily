
from typing import List


class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sum_chalk = sum(chalk)
        
        k = k % sum_chalk
        sum_chalk = [chalk[0]]
        for i in range(1, len(chalk)):
            sum_chalk.append(sum_chalk[i - 1] + chalk[i])
        
        l = 0
        r = len(sum_chalk)
        middle = (r + l) / 2
        while l <= r :
            middle = (r + l) // 2
            if sum_chalk[middle] == k:
                ## 找到了
                return middle + 1
            if sum_chalk[middle] > k:
                r = middle - 1
            else :
                l = middle + 1
        return l

if __name__ == "__main__":
    pass 
    chalk = [6,26,89,39,45,32,71,47,57,47,91,87,86,15,79,82,61,5,17,46,26,93,79,89,18,96,40,60,75,42,60,4,15,48,43,90,62,73,30,81,86,28,98,47,81,78,76,94,27,67,26,28,64,88,50,11,73,81,68,13,97,52,25,39,57,11,17,94]

    k = 233978695
    s = Solution()
    print(s.chalkReplacer(chalk, k))
    