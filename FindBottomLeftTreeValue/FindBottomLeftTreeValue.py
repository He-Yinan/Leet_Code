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
