

from typing import List 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
        left = 0
        right = left + 1
        res = 0
        count = {s[left]: 1}
        max_len = len(s)
        while right < max_len:
            # print(right)
            
            if (k + s[left:right+1].count(max(count, key=count.get))) >= (right + 1 - left) :
                res = right - left + 1
            else :
                count[s[left]] -= 1
                left += 1
            

            if s[right] in count.keys():
                count[s[right]] += 1
            else :
                count[s[right]] = 1

            right += 1
        # print(left, right)
        return res 


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABBB", 2))