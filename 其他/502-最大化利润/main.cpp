#include<iostream>
#include<algorithm>
#include<vector>

using namespace std;

bool sort_func(int i, int j) {
    return i >j;
}

class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        if (k > profits.size())  {
            k = profits.size();
        }
        if (speed_up(w, capital)) {
            int res = w;
            sort(profits.begin(), profits.end(), sort_func);
            for (int i = 0; i < k; i ++) {
                res += profits[i];
            }
            return res;
        } else {
            //贪心 每次找最大的
            for (int i = 0; i < k; i ++) {
                int max_profit = -1;
                int max_position = -1;
                for (int j = 0; j < profits.size(); j ++) {
                    if (w >= capital[j] and profits[j] >= max_profit) {
                        max_profit = profits[j];
                        max_position = j;
                    }
                }

                if (max_position == -1 or max_profit == -1) {
                    break;
                } else {
                    w = w + profits[max_position];
                    // profits.erase(profits.begin() + max_position);
                    // capital.erase(capital.begin() + max_position);
                    capital[max_position] = 1000000000;
                }
                
            }
            return w;
        }
    }

    bool speed_up(int w, vector<int> captial) {
        for (int i = 0; i < captial.size(); i ++) {
            if (w < captial[i]) {
                return false;
            }
        }
        return true ;
    }
};

int main() {
    Solution s = Solution();
    int k = 1;
    int w = 2;
    int p[3] = {1, 2, 3};
    int c[3] = {1, 1, 2};
    vector<int> profits(p, p + 3);
    vector<int> capital(c, c + 3);
    int res = s.findMaximizedCapital(k, w, profits, capital);
    cout<<res<<endl;
}