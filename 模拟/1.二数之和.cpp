
#include<iostream>
#include<vector>
#include<map>

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
            }
        }
        return res;
    }
};



int main() {

    // int a[3] = {1, 2, 3};
    vector<int> a_vec = {1, 2, 3, 4, 5, 6};
    int target = 11;
    
    Solution s = Solution();
    vector<int> res = s.twoSum(a_vec, target);

    for(int i = 0; i < res.size(); i ++) {
        cout<<res[i]<<" ";
    }
    cout<<"hello world"<<endl;
}

