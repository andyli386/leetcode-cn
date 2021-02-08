'''
Author: your name
Date: 2020-11-27 17:40:49
LastEditTime: 2020-11-27 17:43:32
LastEditors: your name
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/9.回文数.py
'''
#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        i = 0
        j = len(str_x)-1
        while i <= j:
            if str_x[i] != str_x[j]:
                return False
            i += 1
            j -= 1
        return True
# @lc code=end

