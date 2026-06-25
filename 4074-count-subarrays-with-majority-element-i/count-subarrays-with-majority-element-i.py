class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)

        arr = [1 if x == target else -1 for x in nums]

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + arr[i]

        ans = 0

        for i in range(n):
            for j in range(i, n):
                if pref[j + 1] - pref[i] > 0:
                    ans += 1

        return ans