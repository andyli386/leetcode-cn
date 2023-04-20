#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # n阶方法数量 = n-1阶+n-2阶
        if n <= 2: return n
        n1 = 1
        n2 = 2
        for i in range(3, n+1):
            s = n1 + n2
            n1 = n2
            n2 = s
        return s

# @lc code=end

