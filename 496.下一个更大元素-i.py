'''
Author: Vincent
Date: 2021-02-21 15:18:34
LastEditors: Vincent
LastEditTime: 2021-02-21 16:24:24
Description: file content
'''
#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1 for _ in range(len(nums2))]
        stack = []
        for i in range(len(nums2)-1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            
            if stack:
                result[i] = stack[-1]

            stack.append(nums2[i])

        res = []
        for i in nums1:
            res.append(result[nums2.index(i)])

        return res
            

# @lc code=end

