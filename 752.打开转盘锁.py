'''
Author: Vincent
Date: 2021-10-07 17:33:54
LastEditors: Vincent
LastEditTime: 2021-10-07 18:04:25
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
        t = s[j]
        if t == '9':
            t = '0'
        else:
            t = int(t)+1
        return s[:j]+str(t)+s[j+1:]
        
    def minusOne(self, s, j):
        t = s[j]
        if t == '0':
            t = '9'
        else:
            t = int(t)-1
        return s[:j]+str(t)+s[j+1:]
        

    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        q = ['0000']
        steps = 0

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q[0]
                q = q[1:]
                if cur in deadends:
                    continue
                if cur == target:
                    return steps

                for j in range(4):
                    up = self.plusOne(cur, j)
                    print(up)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)

                    down = self.minusOne(cur, j)
                    print(down)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            steps += 1

        return -1

# @lc code=end

