# [Leetcode 1038. Binary Search Tree to Greater Sum Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/)

Really interesting medium problem, need to fully understand how *Greater Sum Tree* works and the characteristics of *BST*  

## Method 1 (Smartest)
Use a *global variable* and ***reverted InOrder traversal***!!!

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.cumulative = 0
    #reverted inOrder traversal!!!
    def bstToGst(self, root: TreeNode) -> TreeNode:
        #base case
        if not root:
            return None
        #traverse right
        self.bstToGst(root.right)
        #inOrder adding cumulative sum 
        root.val += self.cumulative
        self.cumulative = root.val
        #traverse left
        self.bstToGst(root.left)

        return root
```

## Method 2 (My method)
My recursive solution which introduces a *helper function* to keep track of the current sum within the recursive function
```python
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # use the idea of RECURSION and solving SUB problems

        # use a helper function with base value to convert to GST 
        # and return the key sum based on base value 
        def helperF(r, base):
            #base case
            if not r:
                return 0
            
            #convert the right subTree to GST first
            rSum = helperF(r.right, base)
            if rSum:
                r.val += rSum
            #for leaf node
            else:
                r.val += base
            
            if r.left:
                #for the left subTree, we use the root.val as the base!!! (key)
                return helperF(r.left, r.val)
            else:
                #otherwise r.val is the key sum of the subTree
                return r.val
        
        #helper function to covert BST to GST
        helperF(root, 0)
        return root
```
