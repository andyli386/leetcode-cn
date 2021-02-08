'''
Author: Vincent
Date: 2021-02-03 23:18:25
LastEditors: Vincent
LastEditTime: 2021-02-04 09:07:16
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
        window = dict()
        for i in p:
            need[i] = need.get(i, 0) + 1

        left = 0; right = 0; valid = 0;

        result = []

        while right < len(s):
            c = s[right]
            right += 1

            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(need):
                    print('valid')
                    result.append(left)

                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return result

        
# @lc code=end

