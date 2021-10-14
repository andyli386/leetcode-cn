'''
Author: Vincent
Date: 2021-10-14 21:38:55
LastEditors: Vincent
LastEditTime: 2021-10-14 21:48:41
Description: file content
'''
#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = dict()
        for i in p:
            need[i] = need.get(i, 0)+1
        window = dict()

        left = 0; right = 0; valid = 0
        res = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
                
            while right - left >= len(p):
                if valid == len(need):
                    res.append(left)
                
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return res          
                
# @lc code=end

