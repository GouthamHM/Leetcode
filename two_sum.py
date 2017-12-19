class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {} # Using Hash table to reduce time complextity from O(n^2) to O(n)
        for ind,val in enumerate(nums):
            com = target-val
            if com in dict:
                return [dict[com],ind]
            else:
                dict[val] = ind

if __name__ =='__main__':
    s = Solution()
    assert s.twoSum([3,2,4],6) ==[1,2]