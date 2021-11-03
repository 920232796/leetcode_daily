

from typing import List 

# 反向思维。
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        pass 
        left = 0
        
        total = len(cardPoints)
        k = total - k 
        right = k - 1
        total_ = sum(cardPoints)
        tmp = sum(cardPoints[left: right + 1])
        res = tmp 
        while left + k < total:
            
            left += 1
            right += 1 
            tmp = tmp + cardPoints[right] - cardPoints[left - 1]

            if tmp < res:
                res = tmp 
            
        return total_ - res 


if __name__ == "__main__":
    s = Solution()
    print(s.maxScore([100,40,17,9,73,75], 3))