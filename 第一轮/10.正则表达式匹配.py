'''
Author: Vincent
Date: 2021-02-06 13:09:32
LastEditors: Vincent
LastEditTime: 2021-02-06 14:55:31
Description: file content
'''
#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = '*'*self.count+' '+str(out)
        print(res+str(out))
    
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s); n = len(p)
        memo = dict()

        def dp(s, i, p, j):
            if j == n:
                return i == m
            if i == m:
                if (n-j) % 2 == 1:
                    return False
                
                for t in range(j, n-1, 2):
                    if p[t+1] != '*':
                        return False
                    
                return True

            if (i, j) in memo:
                return memo[(i,j)]
            
            res = False

            if s[i] == p[j] or p[j] == '.':
                if j < n-1 and p[j+1] == '*':
                    res = dp(s, i, p, j+2) or dp(s, i+1, p, j)
                else:
                    res = dp(s, i+1, p, j+1)
            else:
                if j < n-1 and p[j+1] == '*':
                    res = dp(s, i, p, j+2)
                else:
                    res = False

            memo[(i, j)] = res

            self.count -= 1

            return res
        
        return dp(s, 0, p, 0)

# @lc code=end

# if __name__ == '__main__':
#     s = Solution()
#     print(s.isMatch("b", "b*"))
    