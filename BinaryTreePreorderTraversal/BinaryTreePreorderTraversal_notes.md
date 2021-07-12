# **144.Binary Tree Preorder Traversal**

# Question
Given the root of a binary tree, return the preorder traversal of its nodes' values.

<br/>
Difficulty: Easy

---
# Example test cases
1. Input: root = [1,null,2,3]
Output: [1,2,3]
<br/>
   
2. Input: root = []
Output: []
<br/>

3. Input: root = [1]
Output: [1]
<br/>

4. Input: root = [1,2]
Output: [1,2]
<br/>

5. Input: root = [1,null,2]
Output: [1,2]
---
# Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
---
# Solution
## Thought process:
1. Use a recursive approach. Write a recursive function preorder that could take a list as a input
2. If current node is None, return.
3. Else, append value of root node to ans, do preorder traversal on the left subtree, do inorder traversal on the right subtree. Return the ans.

- Time complexity: O(n) (each tree has n nodes, each node is visited once)
- Space complexity: O(n) (the value of each node needs to be stored in the list ans)
<br/>

## Code:
```python
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
```