#
# @lc app=leetcode.cn id=746 lang=python3
#
# [746] 使用最小花费爬楼梯
#
from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i]表示走到第i个台阶共耗费多少
        dp = [0 for i in range(len(cost)+1)]
        dp[0] = 0
        dp[1] = 0
        for i in range(2, len(cost)+1):
            dp[i] = min(cost[i-1]+dp[i-1], cost[i-2]+dp[i-2])

        return dp[-1]
        # if len(cost) <= 1: return 0

        # dp0 = 0
        # dp1 = 0
        # for i in range(2, len(cost)+1):
        #     s = min(cost[i-1]+dp1, cost[i-2]+dp0)
        #     dp0 = dp1
        #     dp1 = s
        # return dp1

# @lc code=end

