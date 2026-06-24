class Solution(object):
    def splitArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2

            pieces = 1
            curr = 0

            for num in nums:
                if curr + num > mid:
                    pieces += 1
                    curr = num
                else:
                    curr += num

            if pieces <= k:
                right = mid
            else:
                left = mid + 1

        return left