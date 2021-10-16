/*
写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
*/


#include<iostream>
#include<vector>

using namespace std;


class Solution {
public:
    int fib(int n) {
        int f[101] = {0};
        f[0] = 0;
        f[1] = 1;
        for (int i = 2; i <= n; i ++) {
            f[i] = f[i - 2] % 1000000007 + f[i - 1] % 1000000007;
        }
        return f[n] % 1000000007;
    }
};

int main() {

    int n = 100;
    Solution s = Solution();
    cout<<s.fib(n)<<endl;

    cout<<"hello world"<<endl;
}