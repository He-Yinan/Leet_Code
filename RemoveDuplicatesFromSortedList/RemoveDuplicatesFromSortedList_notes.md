# **83. Remove Duplicates from Sorted List**

# Question

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.<br/>
<br/>
Difficulty: Easy
<br/><br/>

# Example test cases
1. Input: head = [1,1,2]<br/>
Output: [1,2]
   
2. Input: head = [1,1,2,3,3]<br/>
Output: [1,2,3]
<br/>

# Constraints
- The number of nodes in the list is in the range [0, 300].
- -100 <= Node.val <= 100
- The list is guaranteed to be sorted in ascending order.

<br/>

# Solution
## Thought process:
1. If linked list is empty or linked list only has one node, return head.
2. Iterate through linked list to check for duplicated value by checking if value of current node is equal to value of previous node. (since linked list is sorted)
3. Duplicate is found, remove the node by linking the previous node to next node.
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
```

# Extra
If the linked list is not sorted, maintain a set and check if value of current node exist in set.
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prevNode = None
        curNode = head
        s = set()
        while curNode != None:
            if curNode.val in s:
                prevNode.next = curNode.next
                curNode = curNode.next
            else:
                s.add(curNode.val)
                prevNode = curNode
                curNode = curNode.next
        return head
```