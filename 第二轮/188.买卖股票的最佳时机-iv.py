'''
Author: Vincent
Date: 2021-10-15 21:28:51
LastEditors: Vincent
LastEditTime: 2021-10-16 16:00:24
Description: file content
'''
#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit_k_inf(self, prices: List[int]) -> int:
        dp_i0 = 0; dp_i1 = -inf
        for i in range(len(prices)):
            temp = dp_i0
            dp_i0 = max(dp_i0, dp_i1+prices[i])
            dp_i1 = max(dp_i1, temp-prices[i])

        return dp_i0

    def maxProfit(self, max_k: int, prices: List[int]) -> int:
        n = len(prices)
        if max_k > n/2:
            return self.maxProfit_k_inf(prices)

        dp = [[[0, -inf] for k in range(max_k+1)] for i in range(n+1)]

        for i in range(n):
            for k in range(max_k, 0, -1):
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-prices[i])

        return dp[n-1][max_k][0]
# @lc code=end
s = Solution()
print(s.maxProfit(2, [2,4,1]))