'''
Author: Vincent
Date: 2021-10-16 13:03:48
LastEditors: Vincent
LastEditTime: 2021-10-16 14:57:33
Description: file content
'''
#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i10 = 0; dp_i11 = -inf
        dp_i20 = 0; dp_i21 = -inf
        for price in prices:
            dp_i20 = max(dp_i20, dp_i21+price)
            dp_i21 = max(dp_i21, dp_i10-price)
            dp_i10 = max(dp_i10, dp_i11+price)
            dp_i11 = max(dp_i11, -price)
        return dp_i20
        
# @lc code=end

