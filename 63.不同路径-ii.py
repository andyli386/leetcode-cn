#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # python中二维数组初始化使用列表生成式，不要使用乘法
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = 1
            else:
                break

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1: continue
                
                dp[i][j] = dp[i-1][j]+dp[i][j-1]

        return dp[m-1][n-1]

# @lc code=end

