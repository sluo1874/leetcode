'''
Created on 2014-3-1

@author: luosai
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
#        A[0] single, A[1] double, A[2] res
        if len(A) == 1:
            return A[0]
        twice = A[1] & A[0]
        once = (A[0] & ~ A[1]) | (A[1] & ~A[0])
        A[0] = once
        A[1] = twice
        for i in range(2, len(A)):
            print str(i) + " A[0]: " + str(A[0]) 
            print str(i) + " A[1]: " + str(A[1]) 
            print str(i) + " A[i]: " + str(A[i]) 
            twice = A[i] & A[0]
            print str(i) + " twice: "+str(twice)
            once = A[i] & ~A[1] &~A[0]
            print str(i) + " once: "+str(once)
            A[0] = A[0] &~twice|once &~(A[1]&A[i])
            A[1] = A[1] & ~(A[1]&A[i]) | twice
            
        
        return A[0]
        
if __name__ == '__main__':
    s = Solution()
    print s.singleNumber([2,2,2,3])
