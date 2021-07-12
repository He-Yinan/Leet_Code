class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        return self.preorder(root, ans)

    def preorder(self, root, ans):
        if not root:
            return
        else:
            # append val of current node
            ans.append(root.val)
            # preorder traversal on left subtree
            self.preorder(root.left, ans)
            # preorder traversal on right subtree
            self.preorder(root.right, ans)
            return ans
