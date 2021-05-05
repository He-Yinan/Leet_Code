# **21. Merge Two Sorted Lists**

# Question

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.<br/>
<br/>
Difficulty: Easy
<br/><br/>

# Example test cases
1. Input: l1 = [1,2,4], l2 = [1,3,4] <br/>
Output: [1,1,2,3,4,4]
   
2. Input: l1 = [], l2 = [] <br/>
Output: []

3. Input: l1 = [], l2 = [0] <br/>
Output: [0]
<br/>

# Constraints
- The number of nodes in both lists is in the range [0, 50].
- -100 <= Node.val <= 100
- Both l1 and l2 are sorted in non-decreasing order.

<br/>

# Solution
## Thought process:
1. Swap l1 and l2 if l1 value is larger than l2 value. Ensure l1 head is the smallest, return l1 at the end of function.
2. Iterate through l1 and l2.
3. If l2_cur value equals to l1_cur value, insert l2_cur node after l1_cur node.
4. If l2_cur value smaller than l1_cur value, considering step 3, it means l2_cur value is between l1_prev value and l1_cur value. Insert l2_cur between them.
5. If l2_cur value larger than l1_cur value, move l1 pointers.
6. If there are still left over nodes in l2 after exiting while loop, it means these leftover nodes are all larger than the last node of l1, append these nodes behind l1.
<br/><br/>
- Time complexity: O(n+m)
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

            # if l2_cur value equals to l1_cur value, insert l2_cur node behind l1_cur node
            if l1_cur.val == l2_cur.val:
                l1_next = l1_cur.next
                l2_next = l2_cur.next
                l1_cur.next = l2_cur
                l2_cur.next = l1_next
                l2_cur = l2_next
                l1_prev = l1_cur
                l1_cur = l1_cur.next
                
            # if l2_cur value smaller than l1_cur value, it means l2_cur value is between
            # l1_prev value and l1_cur value. insert l2_cur between them
            elif l1_cur.val > l2_cur.val:
                l1_prev.next = l2_cur
                l2_next = l2_cur.next
                l2_cur.next = l1_cur
                l2_cur = l2_next
                l1_prev = l1_prev.next

            # if l2_cur value larger than l1_cur value, move l1 pointers
            else:
                l1_prev = l1_cur
                l1_cur = l1_cur.next

        # if there are still left over nodes in l2, it means these nodes are all larger
        # than the last node of l1, append these nodes behind l1 
        if l2_cur != None:
            l1_prev.next = l2_cur
        
        return l1
```