'''
Author: Vincent
Date: 2021-10-07 15:25:26
LastEditors: Vincent
LastEditTime: 2021-10-07 16:00:12
Description: file content
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        track = []
        self.backtrack(nums, track)
        return self.res
        
    def backtrack(self, nums, track):
        if len(track) == len(nums):
            self.res.append(track.copy())
            return 

        for n in nums:
            if n in track:
                continue
            track.append(n)
            self.backtrack(nums, track)
            track.pop()

# @lc code=end

