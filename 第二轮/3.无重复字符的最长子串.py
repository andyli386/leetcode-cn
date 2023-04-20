'''
Author: Vincent
Date: 2021-10-14 22:44:45
LastEditors: Vincent
LastEditTime: 2021-10-14 22:53:29
Description: file content
'''
#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0; right = 0
        res = 0; window = dict()
        while right < len(s):
            c = s[right]
            right += 1

            window[c] = window.get(c, 0) + 1

            while window[c] > 1:
                d = s[left]
                left += 1

                window[d] = window.get(d, 0) - 1
                
            res = max(res, right-left)
        return res

# @lc code=end

