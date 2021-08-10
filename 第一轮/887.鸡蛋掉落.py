'''
Author: Vincent
Date: 2021-02-07 12:31:04
LastEditors: Vincent
LastEditTime: 2021-02-08 13:02:51
Description: file content
'''
#
# @lc app=leetcode.cn id=887 lang=python3
#
# [887] 鸡蛋掉落
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = '*'*self.count+' '+str(out)
        print(res)
    
    # def superEggDrop(self, K: int, N: int) -> int:
    #     memo = dict()

    #     def dp(K, N):
    #         if K == 1: return N
    #         if N == 0: return 0

    #         if (K, N) in memo:
    #             return memo[(K, N)]

    #         res = float('inf')
    #         for i in range(1, N+1):
    #             res = min(res, max(dp(K, N-i), dp(K-1, i-1))+1)

    #         memo[(K, N)] = res

    #         return res
            
    #     return dp(K, N)
            
    def superEggDrop(self, K: int, N: int) -> int:
        memo = dict()
        def dp(K, N):
            # self.count += 1
            if K == 1: return N
            if N == 0: return 0

            if (K, N) in memo:
                return memo[(K, N)]

            res = float('inf')

            # self.printIndent(f'K = {K}, N = {N}')
            lo, hi = 1, N
            while lo <= hi:
                mid = int((lo + (hi-lo)//2))
                broken = dp(K-1, mid-1)
                not_broken = dp(K, N-mid)

                if broken > not_broken:
                    hi = mid-1
                    res = min(res, broken+1)
                else:
                    lo = mid+1
                    res = min(res, not_broken+1)
                    
            memo[(K,N)] = res
            
            return res

        return dp(K, N)


        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.superEggDrop(2, 6))
    # print(s.superEggDrop(4, 200))
    