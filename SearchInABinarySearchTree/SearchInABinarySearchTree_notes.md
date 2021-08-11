# **700. Search in a Binary Search Tree**

# Question
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
<br/>

Difficulty: Easy
<br/>

# Example test cases
1. Input: root = [4,2,7,1,3], val = 2 <br/>
Output: [2,1,3]
```
            4
          /   \
         2     7
        / \
       1   3
```
   
2. Input: root = [4,2,7,1,3], val = 5 <br/>
Output: []
<br/>

# Constraints
- The number of nodes in the tree is in the range [1, 5000].
- 1 <= Node.val <= 107
- root is a binary search tree.
- 1 <= val <= 107
<br/>

# Solution
## Thought process:
1. Do a preorder traversal, check value of the current node for each recursion.
2. If value of current node is equal to val, return the current node.
3. If val is less than current node, do preorder traversal on left subtree.
4. Else, do preorder traversal on right subtree.

Note that BST has the following properties:
- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.
<br/>

- Time complexity: O(n) (traverse the BST with n nodes)
- Space complexity: O(n) (worst case depth of BST is n)
<br/><br/>

## Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None:
            return
        # if target node is found
        if root.val == val:
            return root
        
        # if val is smaller than value of current node
        if val < root.val:
            return self.searchBST(root.left, val)
        
        # if val is larger than value of current node
        return self.searchBST(root.right, val)
```