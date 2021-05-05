# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        # make l1 the linked list with a smaller head
        if l1.val > l2.val:
            temp = l1
            l1 = l2
            l2 = temp
            
        l1_cur = l1
        l2_cur = l2
        l1_prev = None
        
        while l1_cur != None and l2_cur != None:
            if l1_cur.val == l2_cur.val:
                l1_next = l1_cur.next
                l2_next = l2_cur.next
                l1_cur.next = l2_cur
                l2_cur.next = l1_next
                l2_cur = l2_next
                l1_prev = l1_cur
                l1_cur = l1_cur.next
                
            elif l1_cur.val > l2_cur.val:
                l1_prev.next = l2_cur
                l2_next = l2_cur.next
                l2_cur.next = l1_cur
                l2_cur = l2_next
                l1_prev = l1_prev.next

            else:
                l1_prev = l1_cur
                l1_cur = l1_cur.next
                
        if l2_cur != None:
            l1_prev.next = l2_cur
        
        return l1