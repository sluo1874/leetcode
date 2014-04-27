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
        while not start==end:
            if target < matrix[start][0] or target > matrix[end][-1]:
                return False
            mid = end - int(float(end - start)/2)
#            if mid == end:
#                mid = mid - 1
#                end = mid
            if target == matrix[mid][0]:
                return True
            if target < matrix[mid][0]:
                if end == mid:
                    end = end - 1
                else:
                    end = mid
            else:
                start = mid
        
        row = start
        start = 0
        end = len(matrix[row]) - 1
        while not start == end:
            if target < matrix[row][start] or target > matrix[row][end]:
                return False
            mid = end - int(float(end - start)/2)
#            if mid == end:
#                mid = mid - 1
#                end = mid
            if target < matrix[row][mid]:
                if end == mid:
                    end = end - 1
                else:
                    end = mid
                continue
            elif target > matrix[row][mid]:
                start = mid
                continue
            else:
                return True
        if target == matrix[row][start]:
            return True
        else:
            return False
        
if __name__ == '__main__':
    so = Solution()
#    matrix = [[1,3]]
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
    target = 30
    print so.searchMatrix(matrix, target)
    