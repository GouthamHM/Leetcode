class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return 0
        maxLength = 1
        start = 0

        for i in range(len(s)):
            if i-maxLength >= 1 and s[i-maxLength-1:i+1] == s[i-maxLength-1:i+1][::-1]:
                start = i-maxLength-1
                maxLength += 2
                continue
            if i-maxLength >= 0 and s[i-maxLength:i+1] == s[i-maxLength:i+1][::-1]:
                start = i-maxLength
                maxLength +=1
        return s[start:start+maxLength]

if __name__ == '__main__':
    s = Solution()
    print (s.longestPalindrome('abbccbbea'))