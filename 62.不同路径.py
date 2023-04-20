#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # if m == 1 or n == 1: return 1
        # return self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)

        # dp = [[0]*(n+1)]*(m+1)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        dp[1] = [1]*(n+1)
        for item in dp:
            item[1] = 1

        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        
        return dp[m][n]
# @lc code=end

