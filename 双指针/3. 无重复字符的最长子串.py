from typing import List 

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass 
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 
        
        left = -1
        res = 0
        right = 1
        while left < len(s) - 1:
            left = left + 1
            right = left + 1
            while right < len(s):
                if s[right] not in s[left:right]:
                    right = right + 1 
                else :
                    break 
            
            if (right - left) > res:
                res = right - left
        return res        

if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

