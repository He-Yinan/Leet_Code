# **203. Remove Linked List Elements**

# Question

Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.<br/>
<br/>
Difficulty: Easy
<br/><br/>

# Example test cases
1. Input: head = [1,2,6,3,4,5,6], val = 6 <br/>
Output: [1,2,3,4,5]
   
2. Input: head = [], val = 1 <br/>
Output: []

3. Input: head = [7,7,7,7], val = 7 <br/>
Output: []
<br/>

# Constraints
- The number of nodes in the list is in the range [0, 10^4].
- 1 <= Node.val <= 50
- 0 <= k <= 50

<br/>

# Solution
## Thought process:
1. Use a dummy node to point to head in case head needs to be removed
2. Loop through the linked list and check cur.next node
3. If value of cur.next node is equal to val, remove it by connecting cur node to cur.next.next node (jump across cur.next)
4. Else, move cur node to cur.next
<br/><br/>
- Time complexity: O(n)
- Space complexity: O(1)
<br/><br/>

## Code:
```python
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
```