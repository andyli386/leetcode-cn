'''
Author: Vincent
Date: 2021-02-27 01:27:52
LastEditors: Vincent
LastEditTime: 2021-02-27 01:37:19
Description: file content
'''
#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
    def subsets(self, nums: List[int]) -> List[List[int]]:
        track = []
        self.backtrack(nums, 0, track)
        return self.res
    
    def backtrack(self, nums, start, track):
        self.res.append(track.copy())
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, i+1, track)
            track.pop()
# @lc code=end

