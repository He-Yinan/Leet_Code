# **530. Minimum Absolute Difference in BST**

# Question
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Difficulty: Easy

---
# Example test cases
1. Input: root = [4,2,6,1,3]
Output: 1
```
            4
          /   \
         2     6
        / \
       1   3
```
<br/>
   
2. Input: root = [1,0,48,null,null,12,49]
Output: 1

---
# Constraints
- The number of nodes in the tree is in the range [2, 104].
- 0 <= Node.val <= 105
---
# Solution
## Thought process:
1. Perform inorder traversal to get a sorted list values
2. Iterate through list to find the minimum values[i+1] - values[i]

- Time complexity: O(n) (n represents the number of nodes in the BST)
- Space complexity: O(n) (the maximum depth of the tree is n, average case is log(n))

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # get a sorted list from BST
        values = self.inorder(root)

        # find the minumum absolute difference
        min_diff = values[1] - values[0]
        for i in range(1, len(values)-1):
            diff = values[i+1] - values[i]
            if diff < min_diff:
                min_diff = diff
        return min_diff

    # get the sorted list using inorder traversal
    def inorder(self, root):
        if not root:
            return []
        else:
            return self.inorder(root.left) + [root.val] + self.inorder(root.right)
```