# **2. Add Two Numbers**

# Question

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.<br/> <br/>

You may assume the two numbers do not contain any leading zero, except the number 0 itself..<br/>
<br/>
Difficulty: Medium
<br/><br/>

# Example test cases
1. Input: l1 = [2,4,3], l2 = [5,6,4] <br/>
Output: [7,0,8] <br/>
Explanation: 342 + 465 = 807.
   
2. Input: l1 = [0], l2 = [0]< br/>
Output: [0]

3. Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] <br/>
Output: [8,9,9,9,0,0,0,1]
<br/>

# Constraints
- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros.

<br/>

# Solution
## Thought process:
1. Create a new linked list l3 to store the sum
2. Add l1 and l2. If the sum is larger than 9, set carry to 1.
3. If l1 and l2 have different lengths, add the nodes of the linked list with longer length to the carry.
4. If the carry is 1 when all nodes are handled, create new node with value 1 this node will be the last node.
<br/><br/>
- Time complexity: O(max(m,n)) <br/>
  Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.
- Space complexity: O(max(m,n))
<br/><br/>

## Code:
```python
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
```