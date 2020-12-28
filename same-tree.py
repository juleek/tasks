# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None and tree2 != None:
            return False
        if tree1 != None and tree2 == None:
            return False
        
        if tree1.val != tree2.val:
            return False
            
            
        if self.dfs(tree1.left, tree2.left) == False:
            return False
        if self.dfs(tree1.right, tree2.right) == False:
            return False
        return True
    
    
    def isSameTree(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        return self.dfs(tree1, tree2)
