'''
Author: Vincent
Date: 2021-02-03 16:26:45
LastEditors: Vincent
LastEditTime: 2021-02-04 09:01:03
Description: file content
'''
#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start

class Solution:
    count = 0
    debug = False
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
        if self.debug:
            print(res+str(out))

    def minWindow(self, s: str, t: str) -> str:
        window = dict()
        need = dict()
        for i in t:
            need[i] = need.get(i, 0) + 1

        left = 0; right = 0; valid = 0
        
        start = 0
        subLen = len(s)+1

        while right < len(s):
            self.count += 1

            c = s[right]
            right += 1

            # self.printIndent(need)
            # self.printIndent(c)
            if c in need: # 如果c在need中，进行更新
                # self.printIndent('c in need')
                
                window[c] = window.get(c, 0)+1
                if window[c] == need[c]:
                    valid += 1

            # self.printIndent(window)

            while valid == len(need):
                if right - left < subLen:
                    start = left
                    subLen = right - left
                
                d = s[left]
                left += 1

                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] = window.get(d, 0) - 1

        return '' if subLen == len(s)+1 else s[start:start+subLen]

# @lc code=end

