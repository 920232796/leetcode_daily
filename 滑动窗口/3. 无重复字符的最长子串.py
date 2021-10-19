
## 滑动窗口 保持一个 start 一个end变量 
from typing import List 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        if len(s) == 1:
            return 1 
        start = 0
        end = 1
        res = -1
        while end < len(s):
            if s[end] in s[start:end]:
                # 说明出现重复
                r = end - start 
                if r > res :
                    res = r 
                while s[start] != s[end]:
                    start += 1
                start += 1
                end += 1
            else :
                r = end - start + 1
                if r > res:
                    res = r 
                end += 1
        if res == -1:
            return 0
        return res 

        



if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

