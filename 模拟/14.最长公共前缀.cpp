#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        
        int left = 0;
        while (true) {
            string alphabet = "";
            for (int j = 0; j < strs.size(); j ++) {
                if (left >= strs[j].length() || strs[j] == "") {
                    return res;
                }
                if (alphabet == "") {
                    alphabet = strs[j][left];
                } else {
                    if (alphabet[0] != strs[j][left]) {
                        return res;
                    }
                }
            }
            left = left + 1;
            res.push_back(alphabet[0]);
        }

        return res;
    }
};

int main() {

    Solution s = Solution();
    vector<string> str_array;

    // string strs[] = {"flower", "flow", "flight"};
    string strs[] = {"a"};
    for (int i = 0; i < 3; i++) {
        str_array.push_back(strs[i]);
    }
    
    // for (int i = 0; i < str_array.size(); i++) {
    //     cout<<str_array[i]<<endl;
    // }
    string res = s.longestCommonPrefix(str_array);
    cout<<res<<endl;
    // cout<<str_array<<endl;
    return 0;

}