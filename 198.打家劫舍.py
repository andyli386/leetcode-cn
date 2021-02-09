'''
Author: Vincent
Date: 2021-02-09 13:13:47
LastEditors: Vincent
LastEditTime: 2021-02-09 13:32:48
Description: file content
'''
#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     memo = dict()
    #     def dp(nums, start):
    #         if start >= len(nums):
    #             return 0
    #         if start in memo:
    #             return memo[start]
    #         memo[start] = max(dp(nums, start+1), dp(nums, start+2)+nums[start])

    #         return memo[start]

    #     return dp(nums, 0)

    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [0 for _ in range(n+2)]
    #     for i in range(n-1, -1, -1):
    #         dp[i] = max(dp[i+1], dp[i+2]+nums[i])

    #     return dp[0]
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dpi1 = 0; dpi2 = 0
        dpi=0
        for i in range(n-1, -1, -1):
            dpi = max(dpi1, dpi2+nums[i])
            dpi2 = dpi1
            dpi1 = dpi

        return dpi

        
# @lc code=end

