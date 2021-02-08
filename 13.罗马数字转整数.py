'''
Author: your name
Date: 2020-11-27 17:45:11
LastEditTime: 2020-11-27 17:57:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/13.罗马数字转整数.py
'''

#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#


# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        list_s = list(s)
        sum = 0
        pre_num = d[list_s[0]]
        for item in list_s[1:]:
            num = d[item]
            if pre_num < num:
                sum -= pre_num
            else:
                sum += pre_num
            pre_num = num
        sum += pre_num
        return sum


# @lc code=end
