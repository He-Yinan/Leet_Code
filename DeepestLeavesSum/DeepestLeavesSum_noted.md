# **1302. Deepest Leaves Sum**

# Question
Given the root of a binary tree, return the sum of values of its deepest leaves.

Difficulty: Medium

---
# Example test cases
1. Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```
                1
            /       \
           2         3
          / \         \
         4   5         6
        /               \
       7                 8
```
<br/>
   
2. Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19

---
# Constraints
- The number of nodes in the tree is in the range [1, 104].
- 1 <= Node.val <= 100
---
# Solution
## Thought process:
1. Find the depth of the tree
2. Traverse the tree, return sum of the nodes at the deepest level

- Time complexity: O(n) (n represents the number of nodes in the binary tree. Each node is visited twice)
- Space complexity: O(n) (the maximum depth of the tree is n)

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = self.findDepth(root)
        leaves_sum = self.findSum(root, max_depth, 1)
        return leaves_sum

    # find max depth of the tree
    def findDepth(self, root):
        if root is None:
            return 0
        else:
            # find the deeper subtree (left or right) and add 1 (the root node)
            return max(self.findDepth(root.left), self.findDepth(root.right)) + 1

    # find sum of nodes at the max depth (leaves)
    def findSum(self, root, max_depth, depth):
        if root is None:
            return 0
        elif depth == max_depth:
            return root.val
        else:
            # find the sum of all the deepest nodes from both subtrees (left and right)
            return self.findSum(root.left, max_depth, depth+1) + self.findSum(root.right, max_depth, depth+1)

```