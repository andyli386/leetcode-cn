'''
Author: Vincent
Date: 2021-02-03 23:05:52
LastEditors: Vincent
LastEditTime: 2021-02-04 09:03:00
Description: file content
'''
#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = dict()
        need = dict()
        for i in s1:
            need[i] = need.get(i, 0) + 1
        
        left = 0; right = 0; valid = 0

        while right < len(s2):
            c = s2[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            while right - left >= len(s1):
                if valid == len(need):
                    return True

                d = s2[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return False

# @lc code=end

