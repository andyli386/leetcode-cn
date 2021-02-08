'''
Author: Vincent
Date: 2021-02-08 19:55:24
LastEditors: Vincent
LastEditTime: 2021-02-08 22:27:33
Description: file content
'''
#
# @lc app=leetcode.cn id=1049 lang=python3
#
# [1049] 最后一块石头的重量 II
#
from typing import List
# @lc code=start
class Solution:

    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        total = sum(stones)
        target = int(total/2)
        dp = [0 for _ in range(target+1)]

        for i in range(n):
            val = stones[i]

            j = target
            while j>=val: 
                dp[j] = max(
                    dp[j], 
                    dp[j-val]+val)
                    
                j -= 1

        return total - dp[target] - dp[target]
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.lastStoneWeightII([2,7,4,1,8,1]))
    # print(s.lastStoneWeightII([1,2]))
    