
import math 

## 判断奇偶分情况，从中间向两端延伸。

class Solution:
    def longestPalindrome(self, s: str) -> str:

       ## 判断奇偶
        res = ""
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                l = i - j
                r = i + j
                if l < 0 or r > len(s) - 1:
                   # 出界
                   break 
                if s[l] == s[r] and len(s[l:r + 1]) > len(res):
                    # print(f"l is {l}, r is {r}")
                    res = s[l:r+1]
                elif s[l] != s[r]:
                    break 
                
        
        for i in range(0, len(s) - 1):
            for j in range(1, len(s)):
                l = i - j + 1
                r = i + j 
                if l < 0 or r > len(s) - 1:
                   # 出界
                   break 
                if s[l] == s[r] and len(s[l:r + 1]) > len(res):
                    res = s[l:r+1]
                elif s[l] != s[r]:
                    break 

        return res 
                         

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("aacabdkacaa"))

