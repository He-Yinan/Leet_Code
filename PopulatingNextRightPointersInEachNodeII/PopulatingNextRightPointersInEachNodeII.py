"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def levelOrderTraversal(root):
            if root is None:
                return

            # queue: stores nodes that are in one level
            # next_queue: stores nodes that are one level below nodes in queue
            queue = [root]

            while queue:
                for i in range(0, len(queue)):
                    # if the node is not the last one in queue (last one in the level)
                    # link the node to the node on its right
                    if i != len(queue)-1:
                        queue[i].next = queue[i+1]

                next_queue = []
                for node in queue:
                    if node.left is not None:
                        next_queue.append(node.left)
                    if node.right is not None:
                        next_queue.append(node.right)

                queue = next_queue

        levelOrderTraversal(root)
        return root
