'''
Author: Vincent
Date: 2021-02-05 12:11:32
LastEditors: Vincent
LastEditTime: 2021-02-05 13:13:16
Description: file content
'''
#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
        print(res+str(out))
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def dp(i, j):
            # self.count += 1
            # self.printIndent(f'{i} {j} text1 : {text1[:i]}, text2 : {text2[:j]}')
            if i == -1 or j == -1:
                self.count -= 1
                return 0
            if text1[i] == text2[j]:
                return dp(i-1, j-1) + 1
            else:
                return max(dp(i-1, j), dp(i, j-1))

        return dp(len(text1)-1, len(text2)-1)
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     m = len(text1); n = len(text2)
    #     dp = [[0 for i in range(n+1)] for j in range(m+1)]

    #     for i in range(1, m+1):
    #         for j in range(1, n+1):
    #             if text1[i-1] == text2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]+1
    #             else:
    #                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    #     return dp[m][n]
# @lc code=end



