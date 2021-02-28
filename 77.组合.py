'''
Author: Vincent
Date: 2021-02-28 21:30:01
LastEditors: Vincent
LastEditTime: 2021-02-28 21:35:56
Description: file content
'''
#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.res = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k <= 0 or n <=0: return self.res
        track = []
        self.backtrack(n, k, 1, track)

        return self.res

    def backtrack(self, n, k, start, track):
        if k == len(track):
            self.res.append(track.copy())

        for i in range(start, n+1):
            track.append(i)
            self.backtrack(n, k, i+1, track)
            track.pop()


# @lc code=end

