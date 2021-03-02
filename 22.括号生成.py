'''
Author: Vincent
Date: 2021-03-01 19:55:46
LastEditors: Vincent
LastEditTime: 2021-03-02 22:19:28
Description: file content
'''
#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.dp = dict()
    # def generateParenthesis(self, n: int) -> List[str]:
    #     if n in self.dp:
    #         return self.dp[n]
        
    #     if n == 1:
    #         return 1
        
    #     self.dp[n] = self.generateParenthesis(n - 1)

    #     return  int(self.dp[n] * 2 * (2 * n - 1) / (n + 1))

    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0: return {}
        res = []
        track = ''
        self.backtrack(n, n, track, res)

        return res

    def backtrack(self, left, right, track, res):
        if left < 0 or right < 0:
            return 
        if right < left:
            return
        
        if left == 0 and right == 0:
            res.append(track)
            return

        track += '('
        self.backtrack(left-1, right, track, res)
        track = track[:-1]

        track += ')'
        self.backtrack(left, right-1, track, res)
        track = track[:-1]
        
# @lc code=end

