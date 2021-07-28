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
