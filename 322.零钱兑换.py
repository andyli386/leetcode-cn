'''
Author: Vincent
Date: 2021-08-11 11:46:33
LastEditors: Vincent
LastEditTime: 2021-10-07 15:08:34
Description: file content
'''
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = [-888 for i in range(amount+1)]
        return self.dp(coins, amount)


    def dp(self, coins: List[int], amount:int) ->int :
        if amount == 0: return 0
        if amount < 0: return -1
        if self.memo[amount] != -888:
            return self.memo[amount]

        res = inf
        for coin in coins:
            subProblem = self.dp(coins, amount-coin)
            if subProblem == -1: continue
            
            res = min(res, 1+subProblem)
        self.memo[amount] = -1 if res == inf else res
        return self.memo[amount]

# @lc code=end

