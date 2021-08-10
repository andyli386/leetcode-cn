'''
Author: your name
Date: 2021-01-18 20:50:35
LastEditTime: 2021-01-29 08:49:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Users/vincent/Work/projects/onlineproj/leetcode-cn/70.爬楼梯.py
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    climStairsWays = {}
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        if (n-1) not in self.climStairsWays:
            s = self.climbStairs(n-1)
            self.climStairsWays[(n-1)] = s
        
        if (n-2) not in self.climStairsWays:
            s = self.climbStairs(n-2)
            self.climStairsWays[(n-2)] = s

        return self.climStairsWays[n-1] + self.climStairsWays[n-2]

# @lc code=end

