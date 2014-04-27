'''
Created on 2014-4-4

@author: luosai
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if not num:
            return None
        if len(num) == 3:
            root = TreeNode(num[1])
            root.left = TreeNode(num[0])
            root.right = TreeNode(num[2])
            return root
        elif len(num) == 2:
            root = TreeNode(num[0])
            root.right = TreeNode(num[1])
            return root
        elif len(num) == 1:
            return TreeNode(num[0])
        else:
            length = len(num)
            mid = length/2
            root = TreeNode(num[mid])
            root.left = self.sortedArrayToBST(num[0:mid])
            root.right = self.sortedArrayToBST(num[mid+1:])
            return root
    
if __name__ == '__main__':
    so = Solution()
    T = so.sortedArrayToBST([1,2,3,4,5,6,7])
    print T
    