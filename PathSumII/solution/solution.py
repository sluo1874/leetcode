'''
Created on 2014-4-5

@author: luosai
'''
from Tix import Tree
from twisted.lore import tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sumation):
        res = []
        self.findArray(list(), root, sumation, res)
        return res
    
    def findArray(self, arr, root, sumation, res):
        if not root:
            return None
#        print root.val, arr, sumation
        if root and sumation - root.val == 0 and not root.left and not root.right:
            arr.append(root.val)
            res.append(arr)
            return
        else:
            arr.append(root.val)
            self.findArray(list(arr), root.left, sumation-root.val, res)
            self.findArray(list(arr), root.right, sumation-root.val, res)
            
    
if __name__ == '__main__':
    so = Solution()
    x = []
    x.append(1)
#    root = TreeNode(5)
#    root.left = TreeNode(4)
#    root.left.left = TreeNode(11)
#    root.left.left.left = TreeNode(7)
#    root.left.left.right = TreeNode(2)
#    root.right = TreeNode(8)
#    root.right.left = TreeNode(13)
#    root.right.right = TreeNode(4)
#    root.right.right.left = TreeNode(5)
#    root.right.right.right = TreeNode(1)
#    print so.pathSum(root, 22)
    root = TreeNode(-2)
    root.left = TreeNode(-3)
    print so.pathSum(root, -5)
    pass