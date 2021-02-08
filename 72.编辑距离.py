'''
Author: Vincent
Date: 2021-02-05 23:52:33
LastEditors: Vincent
LastEditTime: 2021-02-06 01:26:34
Description: file content
'''
#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
            print(res+str(out))
    
    def minDistance(self, word1: str, word2: str) -> int:
        memo = dict()
        def dp(i, j):
            # self.count += 1
            if (i, j) in memo:
                return memo[(i, j)]
            if i == -1: return j+1
            if j == -1: return i+1

            #  self.printIndent(f' {i} {j} {word1[i]}, {word2[j]}')
            if word1[i] == word2[j]:
                # self.printIndent(f'equal {word1[i]}, {word2[j]}')
                memo[(i, j)] = dp(i-1, j-1)
            else:
                memo[(i, j)] = min([dp(i-1, j-1)+1, dp(i-1, j)+1, dp(i, j-1)+1])
            return memo[(i, j)]

        return dp(len(word1)-1, len(word2)-1)

    # def minDistance(self, word1: str, word2: str) -> int:
    #     m = len(word1); n = len(word2)
    #     dp = [[0 for _ in range(0, n+1)] for _ in range(0, m+1)]


                
# @lc code=end

