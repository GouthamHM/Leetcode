class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows >= len(s) or numRows == 1:
            return s
        list_str = [''] * numRows
        flag = 1
        ind = 0
        for alpha in s:
            list_str[ind] += alpha
            if ind == 0:
                flag = 1
            elif ind == numRows - 1:
                flag = -1
            ind += flag

        return ''.join(list_str)

if __name__ == '__main__':
    s = Solution()
    print(s.convert('abcdefghijkl',4))