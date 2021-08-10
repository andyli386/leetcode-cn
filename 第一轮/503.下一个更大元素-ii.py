'''
Author: Vincent
Date: 2021-02-21 17:18:18
LastEditors: Vincent
LastEditTime: 2021-02-21 17:23:10
Description: file content
'''
#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [-1 for _ in range(size)]
        stack = []

        for i in range(2*size-1, -1, -1):
            while stack and stack[-1] <= nums[i % size]:
                stack.pop()

            if stack:
                result[i % size] = stack[-1]

            stack.append(nums[i % size])

        return result
        
# @lc code=end

