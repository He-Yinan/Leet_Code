# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode()
        l1_cur = l1
        l2_cur = l2
        l3_cur = l3
        carry = 0
        
        # add l1 nodes and l2 nodes
        while l1_cur != None and l2_cur != None:
            val = carry + l1_cur.val + l2_cur.val
            if val >= 10:
                val = val % 10
                carry = 1
            elif carry == 1:
                carry = 0
            
            l3_cur.next = ListNode(val)
            l3_cur = l3_cur.next
            l1_cur = l1_cur.next
            l2_cur = l2_cur.next
        
        # if l1 is longer than l2
        while l1_cur != None:
            val = carry + l1_cur.val
            if val >= 10:
                val = val % 10
                carry = 1
            elif carry == 1:
                carry = 0
            
            l3_cur.next = ListNode(val)
            l3_cur = l3_cur.next
            l1_cur = l1_cur.next
            
        # if l2 is longer than l1
        while l2_cur != None:
            val = carry + l2_cur.val
            if val >= 10:
                val = val % 10
                carry = 1
            elif carry == 1:
                carry = 0
            
            l3_cur.next = ListNode(val)
            l3_cur = l3_cur.next
            l2_cur = l2_cur.next
        
        # add carry to result
        if carry == 1:
            l3_cur.next = ListNode(1)
        
        return l3.next