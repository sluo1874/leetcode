'''
Created on 2014-4-15

@author: luosai
'''

class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        numOfLists = len(matrix)
        if not numOfLists:
            return False
        start = 0
        end = numOfLists - 1
        while True:
            if target < matrix[start][0] or target > matrix[end][0]:
                return False
            
            mid = end - int(float(end - start)/2)
            if mid == end:
                break
            if target < matrix[mid][0]:
                end = mid
            else:
                start = mid

if __name__ == '__main__':
    pass