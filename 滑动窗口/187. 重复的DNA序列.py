from typing import List 


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pass
        start = 0
        end = 9
        res = []
        map_temp = {}
        while end < len(s):
            t = s[start:end + 1]
            if t in map_temp:
                res.append(t)
            else :
                map_temp[t] = 1
            end += 1
            start += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findRepeatedDnaSequences("AAAAAAAAAAA"))