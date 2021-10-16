# Definition for singly-linked list.


from typing import List 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pass
        if head.next is None :
            return None
        head = ListNode(0, next=head)
        forward = head

        return_head = head 
        backward = head 
        for i in range(n):
            forward = forward.next
        # backward = forward

        while forward.next is not None :
            forward = forward.next
            backward = backward.next
        
        backward.next = backward.next.next
        

        return return_head.next



if __name__ == "__main__":
    s = Solution()
    n = 2
    head = ListNode(val=1, next=ListNode(val=2))
    res = s.removeNthFromEnd(head, n)
    while res is not None :
        print(res.val)
        res = res.next