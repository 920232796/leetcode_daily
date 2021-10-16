#include<iostream>
#include<vector>

using namespace std;

class Solution {
    public:
        int search(vector<int>& nums, int target) {
            int left = 0;
            int right = nums.size() - 1;
            int middle;
            while (left <= right) {
                middle = (left + right) / 2;

                if (nums[middle] == target) {
                    //找到了
                    return middle;
                } else if (nums[middle] > target) {
                    right = middle - 1;
                } else {
                    left = middle + 1;
                }
            } 
            return -1;
    }
};


int main() {
    int temp;
    // int num;
    // cin>>num;
    int a[6] = {-1, 0, 3, 5, 9, 12};
    vector<int> vecNum(a, a + 6) ;
    int target = 2;
    // for (int i = 0; i < num; ++i) {
    //     cin >> temp;
    //     vecNum.push_back(temp);
    // }

    for (int i = 0; i < vecNum.size(); i ++) {
        cout<<vecNum[i]<<" ";
    }
    cout<<endl;


    Solution s = Solution();
    int answer = s.search(vecNum, target);
    cout<<"answer is :"<<answer<<endl;
    
}