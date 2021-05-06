# **19. Remove Nth Node From End of List**

# Question

Given the head of a linked list, remove the nth node from the end of the list and return its head.<br/> <br/>
Follow up: Could you do this in one pass?<br/>
<br/>
Difficulty: Medium
<br/><br/>

# Example test cases
1. Input: head = [1,2,3,4,5], n = 2 <br/>
Output: [1,2,3,5]
   
2. Input: head = [1], n = 1 <br/>
Output: []

3. Input: head = [1,2], n = 1 <br/>
Output: [1]
<br/>

# Constraints
- The number of nodes in the list is sz.
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

<br/>

# Solution
## Thought process:
1. Create a dummy node that points to the head in case the head is removed.
2. Move the fast pointer such that is is n jumps apart from cur pointer.
3. Move both fast and cur pointer together until fast pointer is at the last node. cur pointer will be pointing at the n+1th node from the end of the linked list.
4. Link node pointed by cur pointer to the n-1th node from the end of the linked list.
<br/><br/>
- Time complexity: O(sz)
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
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # use a dummy node to cover the case that the head is removed
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
```