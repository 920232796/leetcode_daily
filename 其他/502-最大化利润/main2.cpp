#include<iostream>
#include<vector>
#include<queue>

using namespace std ;

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
            int cur_pro = 0;
            priority_queue<int, vector<int>, less<int> > pq;
            for (int i = 0; i < k; i ++) {
                for (int j = 0; j < profits.size(); j ++) {
                    if (w >= capital[j]) {
                        pq.push(profits[j]);
                    }
                }
                
            }
                
            }
            return w;

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