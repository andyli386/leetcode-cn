'''
Author: Vincent
Date: 2021-02-28 21:50:02
LastEditors: Vincent
LastEditTime: 2021-02-28 22:13:27
Description: file content
'''
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []

        self.backtrack(nums, track)

        return self.res
    
    def backtrack(self, nums, track):
        if len(track) == len(nums):
            self.res.append(track.copy())

            return

        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.backtrack(nums, track)
            track.pop()
        
# @lc code=end

