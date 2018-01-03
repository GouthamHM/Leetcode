class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x>0)-(0>x)
        digits = int(`sign*x`[::-1])
        return (digits*sign *(digits<2**31))

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1230))