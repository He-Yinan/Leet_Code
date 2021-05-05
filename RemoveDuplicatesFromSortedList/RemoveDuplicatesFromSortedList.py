# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        if head.next == None:
            return head
        prevNode = head
        while curNode != None:
            if curNode.val == prevNode.val:
                prevNode.next = curNode.next
                curNode = curNode.next
            else:
                prevNode = curNode
                curNode = curNode.next
        return head