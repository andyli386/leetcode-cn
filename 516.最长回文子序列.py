'''
Author: Vincent
Date: 2021-02-06 11:35:28
LastEditors: Vincent
LastEditTime: 2021-02-06 12:29:40
Description: file content
'''
#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] 最长回文子序列
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
            print(res+str(out))
    
    # def longestPalindromeSubseq(self, s: str) -> int:
    #     n = len(s)
    #     dp = [ [0 if i != j else 1 for j in range(n)] for i in range(n)]
        
    #     for i in range(n-2, -1, -1):
    #         # self.count += 1
    #         for j in range(i+1, n):
    #             # self.printIndent(f'i = {i}, j = {j}')
    #             if s[i] == s[j]:
    #                 dp[i][j] = dp[i+1][j-1]+2
    #             else:
    #                 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    #         # self.count -= 1
            
    #     return dp[0][n-1]
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [1 for i in range(n)]

        for i in range(n-2, -1, -1):
            pre = 0
            for j in range(i+1, n):
                tmp = dp[j]
                if s[i] == s[j]:
                    dp[j] = pre + 2
                else:
                    dp[j] = max(dp[j], dp[j-1])
                pre = tmp
        return dp[n-1]

# @lc code=end

