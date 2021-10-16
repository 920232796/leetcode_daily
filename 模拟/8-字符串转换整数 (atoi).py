
class Solution:
    def myAtoi(self, s: str) -> int:
        
        i = s.strip()
        if len(i) == 0:
            return 0
        if i[0] != "-" and i[0] != "+" and i[0].isdigit() == False:
            return 0
        res = ""
        for j in range(len(i)):
             
            if (j == 0 and (i[j] == "-" or i[j] == "+")) or i[j].isdigit() == True:
                res += i[j]
            else :
                break
        # print(res)
        try:
            i = int(res)
        except:
            return 0
        if i < -2147483648:
            i = -2147483648
        elif i > 2147483647:
            i = 2147483647
        return i 

if __name__ == "__main__":

    s = Solution()
    print(s.myAtoi(" -42+9"))


    # print(2**31)