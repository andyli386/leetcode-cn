'''
Author: your name
Date: 2020-11-24 18:26:56
LastEditTime: 2021-02-02 13:28:57
LastEditors: Vincent
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for item in nums[:-1]:
            sub = target - item
            indx = nums.index(item)
            if sub in nums[indx + 1:]:
                return [indx, nums[indx + 1:].index(sub) + indx + 1]


# @lc code=end