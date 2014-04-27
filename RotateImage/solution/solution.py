'''
Created on 2014-4-4

@author: luosai
'''
from math import sqrt

class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        if not matrix:
            return matrix
        n = len(matrix[0])
        for x in range(0,(n + 1)/2):
            for y in range(0, n/2):
                self.swap(matrix, x, y, y, n-1-x)
                self.swap(matrix, x, y, n-1-x, n-1-y)
                self.swap(matrix, x, y, n-1-y, x)
        return matrix
    def swap(self, matrix, x1, y1, x2, y2):
        matrix[x1][y1] = matrix[x1][y1] - matrix[x2][y2]
        matrix[x2][y2] = matrix[x2][y2] + matrix[x1][y1]
        matrix[x1][y1] = matrix[x2][y2] - matrix[x1][y1]
        
if __name__ == '__main__':
    A = [[1,2, 3],[4, 5, 6], [7, 8, 9]]
    so = Solution()
    so.rotate(A)
    print A
