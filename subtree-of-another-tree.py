# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, tree1: TreeNode, tree2_root: TreeNode) -> bool:
        if self.equal(tree1, tree2_root) == True:
            return True
        if tree1 == None:
            return False
        
        if self.find(tree1.left, tree2_root) == True:
            return True
        if self.find(tree1.right, tree2_root) == True:
            return True
    
        return False
    
    
    def equal(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        if tree1 == None and tree2 == None:
            return True
        if tree1 == None and tree2 != None:
            return False
        if tree1 != None and tree2 == None:
            return False
        if tree1.val != tree2.val:
            return False
        
        if self.equal(tree1.left, tree2.left) == False:
            return False
        if self.equal(tree1.right, tree2.right) == False:
            return False
        return True
    
    def isSubtree(self, tree1: TreeNode, tree2: TreeNode) -> bool:
        return self.find(tree1, tree2)
