'''
Author: Vincent
Date: 2021-10-15 23:14:04
LastEditors: Vincent
LastEditTime: 2021-10-15 23:14:20
Description: file content
'''
#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0; dp_i_1 = -inf
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])

        return dp_i_0
# @lc code=end

