# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if head == None or head.next == None or k == 0:
            return head
        # ------------------------------------------------------
        # reduce k to be less than no_of_node
        no_of_node = 1
        old_last_node = head
        # count number of nodes
        while old_last_node.next != None:
            old_last_node = old_last_node.next
            no_of_node += 1
        # if k is larger than number of nodes, take modulo
        if k >= no_of_node:
            k = k % no_of_node
        # ------------------------------------------------------
        # if k is 0, no change is made
        if k == 0:
            return head
        # ------------------------------------------------------
        # move pointers to correct places
        last_node = head
        first_node = head
        temp_node = head
        # move temp_node ahead k steps first
        while k > 0:
            temp_node = temp_node.next
            k -= 1
        # move first, last and temp node together until temp node is at the end of linked list
        while temp_node.next != None:
            temp_node = temp_node.next
            last_node = last_node.next
            first_node = first_node.next
        # future first node is one after the last node
        first_node = last_node.next
        # ------------------------------------------------------
        # reconnect the nodes
        # last node link to None, first node becomes the head, old last node connects to the previous first node
        old_last_node.next = head
        head = first_node
        last_node.next = None

        return head
