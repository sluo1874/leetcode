'''
Created on 2014-2-27

@author: luosai
'''

class Solution:
    # @return a string
    def convert(self, s, nRows):
        rows = [''] * nRows
        counter = 0
        row = 0
        col = 0
        length_s = len(s) - 1
        if nRows == 1:
            return s
        while True:
            if col % (nRows - 1) == 0:
                rows[row] = rows[row] + s[counter]
                counter += 1
                if counter > length_s:
                    break
                row += 1
                if row % (nRows) == 0:
                    row = 0
                    col += 1
                continue
            else:
                if nRows - (col % (nRows - 1)) - 1 == row:
                    rows[row] += s[counter]
                    counter += 1
                    if counter > length_s:
                        break
                row += 1
                if row % (nRows) == 0:
                    row = 0
                    col += 1
                continue
        res = ""
        for line in rows:
                res += line
        return res
if __name__ == '__main__':
    s = Solution()
    print s.convert("ssartgskkqomcjiaxzgnhfljxmsudswvlxogfgsqygebsmbpoiexpqhmebhhufehespkahcyngbhudzindgevprzqaikfotkiiwkpyjfgmoapnjetrjogcqweajjrevzntkervlzhaaznlficqziupgyrrkiwfkjzwpsrbsabszqfhzhxarspzqirctpifajbpbusvutpwmudnbcnuweuponrhczmckntmjmjehzattfixjvrgbnvqamxcomgybcmlowpvvrrqyznhxfnyskotzoxnagnbicoyafvvymnwobglgtlagcvfqvssbhvljkjjpegotukhvsudohdujbzbwttxcpkmztxqzeesarbxjxaxfftqgsscnlbqclcbebsgfyyhpcebzgagmuxuopxccasfmwisxcyfbzmsdtvezwlnqiiezhibhaivyroytoduprpukkzmgkzyuhdtolwyoftmwjmpapmrjbmvllhsxhsrqvkhjgfznynjkabkrnbaonybafvxooohlaoujtvwtjifjjpawtdmgbpjilgzbxgmxujipehkppqyyhbwaekjhzspmaqpxwexsnfjtmujbmhbvkxwqjhxlbpzbfpzctwwibgbqcmrqwvlgsjxesuptlqvrhuvasrktzmldydtwyhdsqaylwpekgzbnvyqnrajrouupxqlxxospqqapgfzmgcbccrptsymitjxszjswzknqaqhgviudkwfmpxhjvusqdpjcadaanpsnfzwchsgtqlhikorgijylbjpbmrdzhxpmwnpffvayihgtyxbgjzumllpxdtxkqowpbnwikzgtioogoppxqljbwybbtanmomdrzzzkyifjytpmkejcrueovhrohfavrdmqfncfxhowcgimmupeovulclalqcghiuaphcwfkndmtlbfhsjypdjtrlehokrygrpnvluhyxutlxzspkqgqczhndqdphbvaskwghfeezyr",155)
    pass