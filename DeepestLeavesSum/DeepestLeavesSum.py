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
