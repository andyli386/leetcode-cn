'''
Author: Vincent
Date: 2021-02-04 09:11:00
LastEditors: Vincent
LastEditTime: 2021-02-04 11:59:28
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
        window = dict()
        right = 0; left = 0
        maxLen = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c, 0) + 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1

            maxLen = max(maxLen, right-left)

        return maxLen

                
                
# @lc code=end

