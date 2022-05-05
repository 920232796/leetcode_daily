
#include<iostream>
#include<string>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    void addLists(ListNode* res, ListNode* list) {
        while (list != nullptr)
        {
            res -> next = new ListNode(list -> val);
            res = res -> next;
            list = list -> next;
        }
        
    }
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        if (list1 == nullptr) {
            return list2;
        } else if (list2 == nullptr) {
            return list1;
        }
        ListNode* res = new ListNode();
        ListNode* head = res;
        while (list1 != nullptr && list2 != nullptr) {
            if (list1 -> val < list2 -> val) {
                head -> next = new ListNode(list1 -> val);
                list1 = list1 -> next;
            } else {
                head -> next = new ListNode(list2 -> val);
                list2 = list2 -> next;
            }
            head = head -> next;
        }
        if (list1 != nullptr) {
            addLists(head, list1);
        } else {
            addLists(head, list2);
        }

        return res -> next;

    }
};

int main() {

    Solution s = Solution();
    ListNode* list1 = new ListNode(1, new ListNode(3, new ListNode(4, new ListNode(5))));
    ListNode* list2 = new ListNode(2, new ListNode(9, new ListNode(10)));
    ListNode *res = s.mergeTwoLists(list1, list2);

    while (res != nullptr) {
        cout<<res -> val<<endl;
        res = res -> next;
    }

    return 0;
}