'''
Author: Vincent
Date: 2021-02-04 18:15:27
LastEditors: Vincent
LastEditTime: 2021-02-05 09:06:50
Description: file content
'''
#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#

# @lc code=start
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        # 自定义排序规则，对第一维进行排序
        from functools import cmp_to_key
        def sort2dList(x, y):
        # print(f'x = {x}, y = {y}')
            if x[0] == y[0]:
                return 1 if x[1] < y[1] else -1
            elif x[0] < y[0]:
                return -1
            elif x[0] > y[0]:
                return 1
        envelopesSorted = sorted(envelopes, key=cmp_to_key(sort2dList))

        envs = [i[1] for i in envelopesSorted]
        dp = [1 for _ in envs]

        for i in range(len(dp)):
            for j in range(0, i):
                if envs[i] > envs[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
        
# @lc code=end

