'''
Author: your name
Date: 2020-11-30 11:45:36
LastEditTime: 2020-11-30 12:22:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/Users/vincent/Work/projects/onlineproj/leetcode-cn/28.实现-str-str.py
'''
#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        t = 0
        i = 0

        if len(needle) == 0:
            return 0
        if len(needle) > len(haystack):
            return -1

        state = False
        while i < len(haystack):
            if not state:
                t = i
            if haystack[i] == needle[j]:
                j += 1
                state = True
                if j == len(needle):
                    return t
                i += 1
                continue
            else:
                j = 0
                i = t
                state = False
                i += 1
        return -1

# @lc code=end
