'''
Created on 2014-4-4

@author: luosai
'''
class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        twice = False
        num = None
        count = 0
        res = []
        for n in A:
            if num is not None and num == n and twice:
                res.append(n)
                continue
            elif num == n and num is not None:
                count += 1
                twice = True
            elif num is not None:
                num = n
                twice = False
                count += 1
            else:
                num = n
                count += 1
        for n in res:
            A.remove(n)
        return count
            
if __name__ == '__main__':
    so = Solution()
    A = [0,0,0,0,0]
    print so.removeDuplicates(A)
    print A