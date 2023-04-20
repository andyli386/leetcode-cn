#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [1 for i in range(n+1)]
        for i in range(3, n+1):
            for j in range(1, i-1):
                dp[i] =max(dp[i], max(j*dp[i-j], j*(i-j)))

        return dp[n]

# @lc code=end

