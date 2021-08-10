'''
Author: Vincent
Date: 2021-02-07 11:23:24
LastEditors: Vincent
LastEditTime: 2021-02-07 12:29:32
Description: file content
'''
# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = '*'*self.count+' '+str(out)
        print(res)
    
    def maxA(self, N: int)-> int:
        dp = [0]*(N+1)

        for i in range(1, N+1):
            dp[i] = dp[i-1]+1
            self.count += 1
            for j in range(2, i):
                self.printIndent(dp)
                dp[i] = max(dp[i], dp[j-2]*(i-j+1))
                self.printIndent(dp)
            # self.count -= 1

        self.printIndent(dp)
        return dp[N]

if __name__ == '__main__':
    s =  Solution()
    print(s.maxA(9))
    

