# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # dummy node to point to head in case head needs to be removed
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        
        while cur.next:
            # remove cur.next
            if cur.next.val == val:
                # note we do not need to move to next node here as we are always checking cur.next, 
                # which is automatically moved when "cur.next = cur.next.next" is executed
                cur.next = cur.next.next

            # move to next node
            else:
                cur = cur.next
        return dummy.next