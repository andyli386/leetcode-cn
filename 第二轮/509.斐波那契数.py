'''
Author: Vincent
Date: 2021-08-10 12:13:30
LastEditors: Vincent
LastEditTime: 2021-10-07 14:55:57
Description: file content
'''
#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n <= 0: return 0
        if n == 1 or n == 2:
            return 1
        
        pre = 1
        cur = 1
        for i in range(3, n+1):
            total = pre + cur
            pre = cur
            cur = total

        return cur 
# @lc code=end

