'''
Author: Vincent
Date: 2021-01-31 17:51:35
LastEditors: Vincent
LastEditTime: 2021-01-31 18:22:23
Description: file content
'''
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
        print(res+str(out))

    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     memo = {}
    #     def dp(n):
    #         if n in memo: return memo[n]
    #         if n == 0: return 0
    #         if n < 0: return -1
            
    #         res = float('inf')
            
    #         for coin in coins:
    #             subproblem = dp(n-coin)
    #             if subproblem == -1: continue
    #             res = min(res, 1+subproblem)
            
    #         memo[n] = res if res !=float('inf') else -1
    #         return memo[n]

    #     return dp(amount)
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)]
        print(dp)
        dp[0] = 0
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i-coin])
        return -1 if dp[amount] == (amount+1) else dp[amount]

# @lc code=end

