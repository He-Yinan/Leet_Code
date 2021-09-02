# **513. Find Botton Left Tree Value**

# Question

Given the root of a binary tree, return the leftmost value in the last row of the tree.<br/>

Difficulty: Medium

Acceptance: 63.8%

# Example test cases
1. Input: root = [2,1,3]
Output: 1
```
        2
      /   \
     1     3
```
   
2. root = [1,2,3,4,null,5,6,null,null,7] 
Output: 7

# Constraints
- The number of nodes in the tree is in the range [1, 104].
- -231 <= Node.val <= 231 - 1

# Solution
## Thought process:
1. Do level order traversal (first add left child, then right child)
2. Once the next level is empty, break and stop to save the last level in queue
3. Return the value of the 1st node in last level


## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return

        # queue stores the nodes in the current level
        # level stores the nodes that are childen of nodes in queue
        # queue = level to move down one level
        queue = [root]

        while queue:
            level = []

            # add the child nodes of the current level into the next level
            for node in queue:
                if node.left is not None:
                    level.append(node.left)
                if node.right is not None:
                    level.append(node.right)

            # the next level is empyt
            # meaning the level currently stored in queue is the lowest level
            if level == []:
                break
            queue = level

        return queue[0].val
```