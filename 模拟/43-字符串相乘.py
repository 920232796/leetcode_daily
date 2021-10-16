class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1

        res = 0
        for i in range(len(num2)-1, -1, -1):
                zero_num = len(num2)-1 - i
                temp_num1 = int(num1)
                if zero_num != 0:
                    res += temp_num1 * int(num2[i]) * 10**zero_num
                else :
                    res += temp_num1 * int(num2[i])

        return str(res)

if __name__ == "__main__":
    s = Solution()
    print(s.multiply("160", "160"))

    ##16
    ##16
    ##96
    ##160 