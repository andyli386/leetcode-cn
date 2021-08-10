'''
Author: Vincent
Date: 2021-02-21 16:41:54
LastEditors: Vincent
LastEditTime: 2021-02-21 17:15:33
Description: file content
'''
#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0 for _ in range(len(T))]
        stack = [] #存索引 
        for i in range(len(T)-1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i

            stack.append(i)

        return result
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))