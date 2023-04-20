#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        d0 = 0
        d1 =1
        for i in range(2, n+1):
            sum = d0+d1
            d0 = d1
            d1 = sum
        return d1 
# @lc code=end

