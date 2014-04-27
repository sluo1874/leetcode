'''
Created on 2014-2-27

@author: luosai
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        res = ""
        counter = 0
        length_s = len(s)
        if nRows == 1:
            return s
        for i in range(0, nRows):
            counter = 0
            if i == 0:
                while counter * 2 * (nRows - 1) < length_s:
                    res += s[counter * 2 * (nRows - 1)]
                    counter += 1
            elif i == nRows - 1:
                while (counter * 2 + 1) * (nRows - 1) < length_s:
                    res += s[(counter * 2 + 1) * (nRows - 1)]
                    counter += 1
            else:
                counter = 1
                while (counter - 1) * (2 * nRows - 2) + i < length_s:
                    res += s[(counter - 1) * (2 * nRows - 2) + i]
                    if counter * (2 * nRows - 2) - i < length_s:
                        res += s[counter * (2 * nRows - 2) - i]
                    counter += 1
        return res
if __name__ == '__main__':
    s = Solution()
    print s.convert("PAYPALISHIRING",3)
