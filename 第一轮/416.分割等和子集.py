'''
Author: Vincent
Date: 2021-02-08 22:50:52
LastEditors: Vincent
LastEditTime: 2021-02-08 23:17:29
Description: 这题和1049思路一样。如果总数是奇数则不能分割，如果是偶数把总数除以2，设为target，
如果可以凑出总数一半则可以分割。分割时设置一个状态转移数组dp，dp长度为target+1，
dp[j]表示该位置可以存的总和。
'''
#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import List

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums); total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = int(total/2)
        # print(f'target = {target}')

        dp = [0 for _ in range(target+1)]

        for i in range(n):
            # print(f'dp = {dp}')
            val = nums[i]
            j = target
            while j >= val:
                # print(f'j = {j}, val = {val}')
                
                dp[j] = max(dp[j], dp[j-val]+val)
                if dp[j] == target:
                    return True

                j -= 1
        
        return False
        
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.canPartition([1,5, 11, 5]))
    
