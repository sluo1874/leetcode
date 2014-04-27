'''
Created on 2014-4-13

@author: luosai
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        res = []
        rootNodes = []
        while True:
            if not root:
                return res
            if root.left:
                rootNodes.append(root)
                pre = root
                root = root.left
                pre.left = None
                continue
            else:
                res.append(root.val)
            
            if root.right:
                root = root.right
                continue
            elif len(rootNodes) > 0:
                root = rootNodes.pop()
            else:
                return res
if __name__=='__main__':
    so = Solution()
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    print so.inorderTraversal(root)