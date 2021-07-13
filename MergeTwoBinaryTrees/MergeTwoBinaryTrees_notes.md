# **617. Merge Two Binary Trees**

# Question
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.
<br/>

Difficulty: Easy

---
# Example test cases
1. Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
```
            1                       2                           3
         /     \                 /      \                    /     \
       3         2             1          3                4         5
      /                          \          \             /  \         \
     5                            4          7           5    4         7
```
<br/>
   
2. Input: root1 = [1], root2 = [1,2]
Output: [2,2]
<br/>
---
# Constraints
- The number of nodes in both trees is in the range [0, 2000].
- -104 <= Node.val <= 104
---
# Solution
## Thought process:
1. Preorder traverse both trees and merge 2nd tree into 1st tree.
2. If root1 is None, return root2. If root2 is None, return root1.
3. Change the value of current node in 1st tree to the sum of current node value of 1st and 2nd tree.
4. Call mergeTrees recursively using the left node of 1st and 2nd tree and assign the returned value to left node of 1st tree.
5. Call mergeTrees recursively using the right node of 1st and 2nd tree and assign the returned value to right node of 1st tree.

- Time complexity: O(n) (n represents the number of nodes of the merged tree)
- Space complexity: O(n) (the maximum depth of the tree is n, average case is log(n))
<br/>

## Code:
```python
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None:
            return root2
        if root2 == None:
            return root1
            
        # add value of current nodes
        root1.val = root1.val + root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
```