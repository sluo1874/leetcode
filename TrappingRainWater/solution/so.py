class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        if not A:
            return 0
        prePeak = 0
        count = 0
        total = 0
        
        length = len(A)
        for n in range(0, length):
            if n ==0:
                pre = 0
            else:
                pre = A[n-1]
            if n == len(A) - 1:
                post = 0
            else:
                post = A[n+1]
            
            if A[n] >= pre and A[n] > post:
                if count == 0:
                    prePeak = A[n]
                    continue
                if A[n] < prePeak:
                    count += prePeak - A[n]
                    continue
                total += count
                count = 0
                prePeak = A[n]
            else:
                if prePeak is not 0 and A[n] <= prePeak:
                    count += prePeak - A[n]
        count = 0
        prePeak = 0
        for n in range(0, length):
            if n == 0:
                pre = 0
            else:
                pre = A[length - n]
            if n == length - 1:
                post = 0
            else:
                post = A[length - n - 2]
            if A[length - n - 1] >= pre and A[length - n - 1] > post:
                if count == 0:
                    prePeak = A[length - n - 1]
                    continue
                if A[length - n - 1] <= prePeak:
                    count += prePeak - A[length - n - 1]
                    continue
                total += count
                count = 0
                prePeak = A[length - n - 1]
            else:
                if prePeak is not 0 and A[length - n - 1] <= prePeak:
                    count += prePeak - A[length - n - 1]
        return total
    
if __name__ == '__main__':
    so = Solution()
    A = [5,5,1,7,1,1,5,2,7,6]
    print so.trap(A)
    
