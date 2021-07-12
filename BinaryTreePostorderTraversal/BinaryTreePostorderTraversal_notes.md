# **145. Binary Tree Postorder Traversal**

# Question
Given the root of a binary tree, return the postorder traversal of its nodes' values.

<br/>
Difficulty: Easy

---
# Example test cases
1. Input: root = [1,null,2,3]
Output: [3,2,1]
<br/>
   
2. Input: root = []
Output: []
<br/>

3. Input: root = [1]
Output: [1]
<br/>

4. Input: root = [1,2]
Output: [2,1]
<br/>

5. Input: root = [1,null,2]
Output: [2,1]
---
# Constraints
- The number of nodes in the tree is in the range [0, 100].
- -100 <= Node.val <= 100
---
# Solution
## Thought process:
1. Use a recursive approach. Write a recursive function postorder that could take a list as a input
2. If current node is None, return.
3. Else, do postorder traversal on the left subtree, do postorder traversal on the right subtree, append value of root node to ans. Return the ans.

- Time complexity: O(n) (a tree has n nodes, each node is visited once)
- Space complexity: O(n) (the value of each node needs to be stored in the list ans)
<br/>

## Code:
```python
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
```