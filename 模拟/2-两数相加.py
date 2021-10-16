# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        res_next = res
        q = 0
        while l1 is not None and l2 is not None :
            new_res = (l1.val + l2.val + q) % 10
            q = (l1.val + l2.val + q) // 10
           
            res_next.next = ListNode(new_res)
            res_next = res_next.next

            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is not None:
            while l2 is not None:
                l2_val = (l2.val + q) % 10
                q = (l2.val + q) // 10
                    
                # res.append(l2.val)
                res_next.next = ListNode(l2_val)
                res_next = res_next.next
                l2 = l2.next
        if l2 is None and l1 is not None :
            while l1 is not None:
                # print(f"l1.val is {l1.val}")
                # print(f"q is {q}")
                l1_val = (l1.val + q) % 10
                q = (l1.val + q) // 10
                
                # res.append(l1.val)
                res_next.next = ListNode(l1_val)
                res_next = res_next.next
                l1 = l1.next
        # print(q)
        if q != 0:
            res_next.next = ListNode(1)
    
        return res.next 



        
        



if __name__ == "__main__":
    s = Solution()
    # l1 = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9)))))))
    # l2 = ListNode(9, next=ListNode(9, next=ListNode(9, next=ListNode(9))))
    l1 = ListNode(2, next=ListNode(4, next=ListNode(9)))
    l2 = ListNode(5, next=ListNode(6, next=ListNode(4, next=ListNode(9))))

    res = s.addTwoNumbers(l1, l2)


    while res is not None :
        print(res.val)
        res = res.next