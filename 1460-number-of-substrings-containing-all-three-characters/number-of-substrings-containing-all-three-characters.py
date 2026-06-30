class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        p = [-1, -1, -1]
        total = 0

        for i in range(len(s)):
            p[ord(s[i]) - ord('a')] = i
            total += min(p) + 1

        return total
