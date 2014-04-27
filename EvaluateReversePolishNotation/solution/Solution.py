'''
Created on 2014-4-13

@author: luosai
'''

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        if not tokens:
            return 0
        res = []
        while tokens:
            digit = tokens.pop(0)
            if digit.isdigit() or (digit[0]=='-' and digit[1:].isdigit()):
                res.append(int(digit))
            else:
                d1=res.pop()
                d2=res.pop()
                if digit == '/':
                    res.append( int(float(d2)/d1) )
                elif digit == '+':
                    res.append(d2+d1)
                elif digit == '-':
                    res.append(d2-d1)
                else:
                    res.append(d2*d1)
        return res[0]
                    

if __name__ == '__main__':
    so = Solution()
#    print int('-4')
    print so.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])