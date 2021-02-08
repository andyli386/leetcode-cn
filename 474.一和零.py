'''
Author: Vincent
Date: 2021-02-08 23:18:28
LastEditors: Vincent
LastEditTime: 2021-02-09 00:58:46
Description: file content
'''
#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#
from typing import List
# @lc code=start
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for s in strs:
            val0 = sum([1 if d == '0' else 0 for d in s])
            val1 = sum([1 if d == '1' else 0 for d in s])
            zeros = m
            while zeros >= val0:
                ones = n
                while ones >= val1:
                    dp[zeros][ones] = max(dp[zeros][ones], dp[zeros-val0][ones-val1]+1)

                    ones -= 1
                zeros -= 1

        return dp[m][n]

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    # s.findMaxForm(strs = ["10", "0", "1"], m = 1, n = 1)
    # print(s.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))
    print(s.findMaxForm(strs = ["10", "0", "1"], m = 1, n = 1))
    