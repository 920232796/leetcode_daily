from typing import List



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pass
        version1 = version1.split(".")
        version2 = version2.split(".")

        min_l = min(len(version1), len(version2))
        for i in range(min_l):
            v1 = version1[i].lstrip("0") + "1"
            v2 = version2[i].lstrip("0") + "1"
            if v1 == v2 :
                continue
            if int(v1) > int(v2):
                return 1
            else :
                return -1
        q = []
        if len(version1) > len(version2):
            q = version1[min_l:]
            for qq in q :
                qq = qq.lstrip("0") + "1"
                if int(qq) == 1:
                    continue
                if int(qq) > 1:
                    return 1 
                
        elif len(version2) > len(version1) :
            q = version2[min_l:]
            for qq in q :
                qq = qq.lstrip("0") + "1"
                if int(qq) == 1:
                    continue
                if int(qq) > 1:
                    return -1
        

        return 0    

if __name__ == "__main__":

    s = Solution()
    print(s.compareVersion("1.0.1", "1"))


    # s1 = "000"
    # print(s1.lstrip("0"))
    