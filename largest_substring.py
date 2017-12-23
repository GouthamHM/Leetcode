class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        hash_s = {}  #Storing the substring in a hash table

        for ind, char in enumerate(s):
            #checkig if character is already in substring
            #and start value is less than index of the character
            if char in hash_s and start <= hash_s[char]:
                start = hash_s[char] + 1
            #if not just update the maxlength and keep moving
            else:
                maxLength = max(maxLength, ind - start + 1)
            #set the value of hashtable on every iteration
            hash_s[char] = ind
        return maxLength

if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring('abcdabc') is 4