class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        MAX = (2**31)-1
        MIN = -1*(2**31)
        str = str.strip()
        str = re.findall('^[+\\-]?\\d+',str)
        try:
            res = int(''.join(str))
            if res >MAX:
                return MAX
            elif res<MIN:
                return MIN
            return res
        except:
            return 0

if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi(' s-2001'))