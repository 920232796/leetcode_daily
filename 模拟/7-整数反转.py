
class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2147483647
        min_int = -2147483648
        res = 0 
       
        if x < 0:
            flag = 1
            x = -x 
        while x > 0 :
            res = res * 10 + x % 10
            # print(x % 10)
            x = x // 10
        
        if flag == 1:
            res = -res 
        if res > max_int or res < min_int:
            return 0
        return res


if __name__ == "__main__":
    print("hello")
    s = Solution()
    # print(s.reverse(-123))
    print(-11 % 10)