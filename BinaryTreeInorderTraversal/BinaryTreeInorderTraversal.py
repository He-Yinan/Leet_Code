class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        return self.inorder(root, ans)

    def inorder(self, root, ans):
        if not root:
            return
        else:
            # inorder traverse left subtree
            self.inorder(root.left, ans)
            ans.append(root.val)
            # inorder traverse right subtree
            self.inorder(root.right, ans)
            return ans
