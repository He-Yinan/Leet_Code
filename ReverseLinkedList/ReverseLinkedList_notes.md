# **206. Reverse Linked List**

# Question
Given the head of a singly linked list, reverse the list, and return the reversed list.<br/>
<br/>
Difficulty: Easy
<br/><br/>

# Example test cases
1. Input: head = [1,2,3,4,5]<br/>
Output: [5,4,3,2,1]
   
2. Input: head = [1,2]<br/>
Output: [2,1]
   
3. Input: head = []<br/>
Output: []
<br/>

# Constraints
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

<br/>

# Solution
## Thought process:
1. if linked list is empty, return head
2. to reverse each link, update nextNode, change curNode.next to prevNode, move prevNode to curNode and curNode to nextNode.
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
    def reverseList(self, head: ListNode) -> ListNode:
        # if linked list is empty, return head
        if head == None:
            return head
        
        prevNode = None
        curNode = head
        while curNode != None:
            nextNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            
        return prevNode
```