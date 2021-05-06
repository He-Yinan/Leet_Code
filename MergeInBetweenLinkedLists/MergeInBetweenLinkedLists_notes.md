# **1669. Merge In Between Linked Lists**

# Question

You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.<br/>
<br/>
Difficulty: Medium
<br/><br/>

# Example test cases
1. Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002] <br/>
Output: [0,1,2,1000000,1000001,1000002,5] <br/>
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
   
2. Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004] <br/>
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6] <br/>
Explanation: The blue edges and nodes in the above figure indicate the result.
<br/>

# Constraints
- 3 <= list1.length <= 104
- 1 <= a <= b < list1.length - 1
- 1 <= list2.length <= 104

<br/>

# Solution
## Thought process:
1. Create a dummy node that points to head node to cover the case that the head node is removed
2. Let cur_a travel to the node before the 1st node being removed.
3. Let cur_b travel to the second last node that needs to be removed.
4. Let cur_b travel to the 1st node that is after the nodes that are removed
5. cur_a.next = list2
6. Let cur_2 travel to the last node in list2.
7. cur_2.next = cur_b
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
```