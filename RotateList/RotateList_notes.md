# **61. Rotate List**

# Question

Given the head of a linked list, rotate the list to the right by k places.<br/>
Difficulty: Medium

---

# Example test cases
1. Input: head = [1,2,3,4,5], k = 2 <br/>
Output: [4,5,1,2,3] <br/>
```
              1 -> 2 -> 3 -> 4 -> 5
    Rotate 1  5 -> 1 -> 2 -> 3 -> 4
    Rotate 2  4 -> 5 -> 1 -> 2 -> 3
```
   
2. head = [0,1,2], k = 4 <br/>
Output: [2,0,1]

---

# Constraints
- The number of nodes in the list is in the range [0, 500].
- -100 <= Node.val <= 100
- 0 <= k <= 2 * 109

---

# Solution
## Thought process:
1. If head is None or there is only one node or k is 0, return the head.
2. If the k is larger than number of nodes, let k = k % no_of_node.
3. If reduced k = 0, return head.
4. Create pointers last_node, first_node, temp_node. Move them to their correct places.
5. Reconnect the nodes. Link old last node to previous first node, link head to first node, last node link to None.

Pointers used:
- old_last_node: used to count number of nodes by traversing the link list and marks the last node of the linked list before rotation.
- last_node: marks the last node of the linked list after rotation.
- first_node: marks the first node of the linked list after rotation.
- temp_node: helps to find the location of last_node.

<br/>

- Time complexity: O(n) where n is the number of nodes of the linked list <br/>
- Space complexity: O(1)
<br/>

## Code:
```python
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
```