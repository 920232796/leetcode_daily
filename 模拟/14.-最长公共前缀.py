from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_l = min([len(s) for s in strs])
        res = ""
        if len(strs) == 1:
            return strs[0]
        
        for i in range(min_l):
            last = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] == last:
                    last = strs[j][i]
                    if j == len(strs) - 1:
                        res += last
                else :
                    return res

        return res

if __name__ == "__main__":
    print("hello")
    s = Solution()
    print(s.longestCommonPrefix(["aa", "bb", "cc"]))