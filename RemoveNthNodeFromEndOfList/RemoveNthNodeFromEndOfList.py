# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        fast = dummy
        
        count = 1

        # move fast pointer such that it is n jumps apart from cur
        while count <= n:
            fast = fast.next
            count += 1
        
        # move both fast and cur pointer until fast pointer is at the end
        # cur pointer will be at n+1th node from end of the linked list
        while fast.next != None:
            fast = fast.next
            cur = cur.next
        
        cur.next = cur.next.next
        return dummy.next