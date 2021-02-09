'''
Author: Vincent
Date: 2021-02-09 12:33:40
LastEditors: Vincent
LastEditTime: 2021-02-09 13:04:40
Description: file content
'''
#
# @lc app=leetcode.cn id=518 lang=python3
#
# [518] 零钱兑换 II
#
from typing import List
# @lc code=start
class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
    #     n = len(coins)
    #     dp = [[0 if j != 0 else 1 for j in range(amount+1)] for i in range(n+1)]
        
    #     for i in range(1, n+1):
    #         for j in range(1, amount+1):
    #             if j - coins[i-1] >= 0:
    #                 dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
    #             else:
    #                 dp[i][j] = dp[i-1][j]
    #     return dp[n][amount]
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0 if _ != 0 else 1 for _ in range(amount+1)]
        
        for i in range(1, n+1):
            for j in range(1, amount+1):
                if j - coins[i-1] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i-1]]
                    
        return dp[amount]

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1,2,5]))
    
