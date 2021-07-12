class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        return self.postorder(root, ans)

    def postorder(self, root, ans):
        if not root:
            return
        else:
            # postorder traversal on left subtree
            self.postorder(root.left, ans)
            # postorder traversal on right subtree
            self.postorder(root.right, ans)
            # append val of current node
            ans.append(root.val)
            return ans
