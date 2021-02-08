'''
Author: Vincent
Date: 2021-02-02 09:02:19
LastEditors: Vincent
LastEditTime: 2021-02-02 09:17:19
Description: file content
'''
#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def plusOne(self, s, j):
        if s[j] == '9':
            s = s[:j]+'0'+s[j+1:]
        else:
            s = s[:j] + str(int(s[j])+1) + s[j+1:]
        return s

    def minusOne(self, s, j):
        if s[j] == '0':
            s = s[:j]+'9'+s[j+1:]
        else:
            s = s[:j] + str(int(s[j])-1) + s[j+1:]
        return s


    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        q = []
        q.append('0000')
        visited.add('0000')

        step = 0

        while len(q):
            for i in range(len(q)):
                current = q[0]
                q = q[1:]

                if current in deadends:
                    continue

                if current == target:
                    return step

                for j in range(4):
                    plus = self.plusOne(current, j)
                    if not plus in visited:
                        q.append(plus)
                        visited.add(plus)

                    minus = self.minusOne(current, j)
                    if not minus in visited:
                        q.append(minus)
                        visited.add(minus)
            step += 1
            
        return -1


# @lc code=end

