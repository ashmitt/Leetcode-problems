class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ln = 0
        c = []

        for i in range(len(nums)):
            if nums[i] == 1:
                ln += 1
            else:
                c.append(ln)
                ln = 0
            c.append(ln)
        return max(c)
                