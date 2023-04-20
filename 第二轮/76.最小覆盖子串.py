'''
Author: Vincent
Date: 2021-10-14 14:26:09
LastEditors: Vincent
LastEditTime: 2021-10-14 18:22:10
Description: file content
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        need = dict()
        for i in t:
            need[i] = need.get(i, 0) + 1
        
        left = 0; right = 0; valid = 0
        start = 0; length = len(s)+1

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0)+1
                if window[c] == need[c]:
                    valid += 1
                
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0)-1
        return "" if length == len(s)+1 else s[start:start+length]

        
# @lc code=end

