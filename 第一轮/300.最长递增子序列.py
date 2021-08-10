'''
Author: Vincent
Date: 2021-02-04 12:07:02
LastEditors: Vincent
LastEditTime: 2021-02-04 13:28:00
Description: file content
'''
#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     dp = [1 for _ in nums]

    #     for i in range(len(nums)):
    #         for j in range(0 , i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j]+1)

    #     return max(dp)

    def lengthOfLIS(self, nums: List[int]) -> int:
        top = [-1 for _ in nums]
        piles = 0
        for i in range(len(nums)):
            poker = nums[i]

            left = 0; right = piles
            while left < right:
                mid = int(left + (right-left)/2)
                if top[mid] > poker:
                    right = mid
                elif top[mid] < poker:
                    left = mid + 1
                elif top[mid] == poker:
                    right = mid
            
            if left == piles : piles += 1
            top[left] = poker
        return piles
    
# @lc code=end

