'''
Author: Vincent
Date: 2021-10-16 15:06:10
LastEditors: Vincent
LastEditTime: 2021-10-16 15:07:32
Description: file content
'''
#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i0 = 0; dp_i1 = -inf
        for price in prices:
            temp = dp_i0
            dp_i0 = max(dp_i0, dp_i1+price)
            dp_i1 = max(dp_i1, temp-price-fee)
            
        return dp_i0
# @lc code=end

