'''
Author: your name
Date: 2020-11-29 12:16:04
LastEditTime: 2020-11-29 18:05:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/20.有效的括号.py
'''
#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
from typing import Tuple


class Solution:
    def isValid(self, s: str) -> bool:
        pair_dict = {'(': ')', '{': '}', '[': ']', '?': '?'}
        t_list = ['?']
        for item in s:
            if item in pair_dict:
                t_list.append(item)
            else:
                t = t_list.pop()
                if pair_dict[t] != item:
                    return False
        return len(t_list) == 1


# @lc code=end
