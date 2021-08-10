'''
Author: your name
Date: 2020-11-27 18:00:16
LastEditTime: 2020-11-29 11:55:07
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/14.最长公共前缀.py
'''
#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        num = min([len(item) for item in strs])
        for i in range(num):
            c = strs[0][i]
            for item in strs[1:]:
                if item[i] != c:
                    return item[:i]
        return strs[0][:num]
            
# @lc code=end

