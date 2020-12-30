# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.result = 0
        
    def longest(self, tree: TreeNode) -> int:
        if tree == None:
            return 0
        left: int = self.longest(tree.left)
        right: int = self.longest(tree.right)
            
        self.result = max(self.result, left + right)
        return 1 + max(left, right)

    
    def diameterOfBinaryTree(self, tree: TreeNode) -> int:
        if tree == None:
            return 0
        self.longest(tree)
        return self.result
