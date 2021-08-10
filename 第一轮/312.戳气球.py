'''
Author: Vincent
Date: 2021-02-08 13:03:06
LastEditors: Vincent
LastEditTime: 2021-02-08 15:41:30
Description: file content
'''
#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
from typing import List
# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = '*'*self.count+' '+str(out)
        print(res)
    
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        points = [0 for i in range(n+2)]
        points[0] = 1
        points[n+1] =1
        for i in range(1, n+1):
            points[i] = nums[i-1]

        # self.printIndent(points)
        dp = [[0 for i in range(n+2)] for j in range(n+2)]
        # self.printIndent(dp)

        for i in range(n, -1, -1):
            self.count += 1
            # self.printIndent(f'i = {i}')
            # self.printIndent(dp)

            for j in range(i+1, n+2):
                # self.count += 1
                # self.printIndent(f'j = {j}')
                # self.printIndent(dp)

                for k in range(i+1, j):
                    # self.count += 1
                    # self.printIndent(f'i = {i}, j = {j}, k = {k}, dp[{i}][{j}] = {dp[i][j]}, dp[{i}][{k}] = {dp[i][k]}, dp[{k}][{j}] = {dp[k][j]}')
                    # self.printIndent(dp)
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+points[i]*points[j]*points[k])
                    # self.printIndent(dp)
                    # self.count -= 1

                # self.count -= 1
            # self.count -= 1

        return dp[0][n+1]
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.maxCoins([3,8]))
    