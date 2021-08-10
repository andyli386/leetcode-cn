'''
Author: Vincent
Date: 2021-02-22 16:33:34
LastEditors: Vincent
LastEditTime: 2021-02-22 17:07:36
Description: file content
'''
#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start

class MonotonicQueue:
    def __init__(self) -> None:
        self.que = []

    def push(self, n):
        while self.que and self.que[-1] < n:
            self.que.pop()
        self.que.append(n)

    def pop(self, n):
        if n == self.que[0]:
            self.que.pop(0)

    def max(self):
        return self.que[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []
        for i in range(len(nums)):
            if i < k-1:
                window.push(nums[i])
            else:
                window.push(nums[i])

                res.append(window.max())

                window.pop(nums[i-k+1])
                
        return res
# @lc code=end

