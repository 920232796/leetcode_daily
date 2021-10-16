
from typing import List 

class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        start = 0
        while start + 2 * k < len(s):
            s = self.reverse(s, start, start + k - 1)
            start = start + 2 * k
        if start + k > len(s):
            # 剩余字符小于k，全部反转
            s = self.reverse(s, start, len(s) - 1)
            
        else :
            # start + 2k > len(s)
            s = self.reverse(s, start, start + k - 1)
        return s 

    def reverse(self, str, i, j):
        str_l = list(str)
        while i < j:
            str_l[i], str_l[j] = str_l[j], str_l[i]
            i = i + 1
            j = j - 1
        return "".join(str_l)


if __name__ == "__main__":
    s = Solution()
    print(s.reverseStr("abcdefg", 2))


    