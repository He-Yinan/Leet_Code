# **235. Lowest Common Ancestor of a Binary Search Tree**

# Question
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
<br/>

Difficulty: Easy
<br/>

# Example test cases
1. Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8<br/>
Output: 6<br/>
Explanation: The LCA of nodes 2 and 8 is 6.
```
            6
          /   \
        2       8
       / \     / \
      0   4   7   9
         / \
        3   5
```
   
2. Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4 <br/>
Output: 2 <br/>
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition. <br/>

3. Input: root = [2,1], p = 2, q = 1 <br/>
Output: 2 <br/>

# Constraints
- The number of nodes in the tree is in the range [2, 105].
- -109 <= Node.val <= 109
- All Node.val are unique.
- p != q
- p and q will exist in the BST.
<br/>

# Solution
## Thought process:
1. Traverse the BST, each recursion approaching p and q.
2. Return root when p is on one side of root and q is on the other side of root.

Note that BST has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
<br/>

- Time complexity: O(n) (traverse the BST with n nodes, worst case traverse all nodes)
- Space complexity: O(m) (m is the depth of BST)
<br/><br/>

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if both p and q are smaller than root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # if both q and q are larger than root
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # if p is on one side of root, q is on the other side
        else:
            return root

```