# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # use a dummy node to cover the case that the head node is removed
        dummy = ListNode()
        dummy.next = list1
        cur_a = dummy
        cur_b = dummy
        count = 0
        cur_2 = list2
        
        # let cur_a and cur_b travel to their place
        while count != b:
            # cur_b continue to travel when cur_ a is already in place
            if count >= a:
                cur_b = cur_b.next
            # both cur_b and cur_a moves
            else:
                cur_a = cur_a.next
                cur_b = cur_b.next
            count += 1

            # let pointer of cur_2 make use of this loop and also travel
            if cur_2.next != None:
                cur_2 = cur_2.next
        
        # move cur_b to the 1st node after the part being removed
        cur_b = cur_b.next.next
        cur_a.next = list2
        
        # make sure cur_2 travels to the last node of list2
        while cur_2.next != None:
            cur_2 = cur_2.next
        
        cur_2.next = cur_b
        
        return dummy.next