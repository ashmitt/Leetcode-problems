#My solution not working that's why copy-pasted from solutions 

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(m):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD


'''class Solution(object):
    def zigZagArrays(self, n, l, r):
        """
        :type n: int
        :type l: int
        :type r: int
        :rtype: int
        """
        MOD = 10**9 + 7
        m = r - l + 1

        # For length 1, each value can start a sequence.
        up = [1] * m
        down = [1] * m

        for _ in range(1, n):
            new_up = [0] * m
            new_down = [0] * m

            # Prefix sums of up
            prefix = [0] * m
            prefix[0] = up[0]
            for i in range(1, m):
                prefix[i] = (prefix[i - 1] + up[i]) % MOD

            # Suffix sums of down
            suffix = [0] * m
            suffix[m - 1] = down[m - 1]
            for i in range(m - 2, -1, -1):
                suffix[i] = (suffix[i + 1] + down[i]) % MOD

            for y in range(m):
                # Previous value smaller than y
                if y > 0:
                    new_down[y] = prefix[y - 1]

                # Previous value greater than y
                if y < m - 1:
                    new_up[y] = suffix[y + 1]

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD

        '''