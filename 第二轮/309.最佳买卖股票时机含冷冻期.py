'''
Author: Vincent
Date: 2021-10-16 15:03:14
LastEditors: Vincent
LastEditTime: 2021-10-16 15:05:02
Description: file content
'''
#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i0 = 0; dp_i1 = -inf
        dp_pre0 = 0
        for price in prices:
            temp = dp_i0
            dp_i0 = max(dp_i0, dp_i1+price)
            dp_i1 = max(dp_i1, dp_pre0-price)
            dp_pre0 = temp
        return dp_i0
# @lc code=end

