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
