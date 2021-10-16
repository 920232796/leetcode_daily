#include<iostream>
#include<map>
#include<vector>


using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        map<int, int> m;
        for (int i = 0; i < nums.size(); i ++) {
            if (m.find(target - nums[i]) == m.end()) {
                m[nums[i]] = i;
            } else {
                res.push_back(i);
                res.push_back(m[target - nums[i]]);
                return res ;
            }
        }
        return res;
    }
};

int main() {

    Solution s = Solution();
    int a[3] = {2, 7, 9};
    vector<int> aa(a, a + 3);
    vector<int> res = s.twoSum(aa, 9);
    for (int i = 0; i < res.size(); i ++) {
        cout<<res[i]<<" ";

    }
    cout<<endl;
     
}