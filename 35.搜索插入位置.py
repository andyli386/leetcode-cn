'''
Author: your name
Date: 2020-12-04 12:20:50
LastEditTime: 2020-12-06 12:19:54
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/Users/vincent/Work/projects/onlineproj/leetcode-cn/35.搜索插入位置.py
'''
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(0, len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)

# @lc code=end

