#include<iostream>
#include<string>
#include<stack>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '{') {
                st.push('}');
            } else if (s[i] == '[') {
                st.push(']');
            } else if (s[i] == '(') {
                st.push(')');
            } else {
                if (st.empty()) {
                    return false;
                }
                if (s[i] != st.top()) {
                    return false;
                } else {
                    st.pop();
                }
            }
        }
        if (!st.empty()) {
            return false;
        }
        return true;
    }
};


int main() {

    Solution s = Solution();

    string ss = "{{}}{()}";
    cout<<s.isValid(ss)<<endl;

    return 0;
}