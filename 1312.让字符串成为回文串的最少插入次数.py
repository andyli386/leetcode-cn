'''
Author: Vincent
Date: 2021-02-06 12:43:38
LastEditors: Vincent
LastEditTime: 2021-02-06 13:04:14
Description: file content
'''
#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution:
    # def minInsertions(self, s: str) -> int:
    #     n = len(s)
    #     dp = [[0 for j in range(n)] for i in range(n)]

    #     for i in range(n-2, -1, -1):
    #         for j in range(i+1, n):
    #             if s[i] == s[j]:
    #                 dp[i][j] = dp[i+1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i+1][j], dp[i][j-1])+1

    #     return dp[0][n-1]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]

        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre
                else:
                    dp[j] = min(dp[j], dp[j-1])+1

                pre = tmp
        
        return dp[n-1]

# @lc code=end

