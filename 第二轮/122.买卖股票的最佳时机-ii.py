'''
Author: Vincent
Date: 2021-10-16 12:50:23
LastEditors: Vincent
LastEditTime: 2021-10-16 13:02:19
Description: file content
'''
#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0; dp_i_1 = -inf
        for i in range(len(prices)):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1+prices[i])
            dp_i_1 = max(dp_i_1, temp-prices[i])

        return dp_i_0
# @lc code=end

