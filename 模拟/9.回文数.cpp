
#include<iostream>
#include<vector>
#include<string>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        string x_string = to_string(x);
        int left = 0;
        int right = x_string.length() - 1;
        while (left < right) {
            if (x_string[left] != x_string[right]) {
                return false;
            }
            left = left + 1;
            right = right - 1;
        }
        return true;
    }
};

int main() {

    Solution s = Solution();
    cout<<s.isPalindrome(123)<<endl;

}