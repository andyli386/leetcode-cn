'''
Author: your name
Date: 2021-01-21 22:03:24
LastEditTime: 2021-01-27 08:44:22
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /undefined/Users/vincent/Work/projects/onlineproj/leetcode-cn/67.二进制求和.py
'''
#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        length = len(a) if len(a) > len(b) else len(b)
        if len(a) > len(b):
            t = a
            a = b
            b = t
        result = ''
        carry = 0

        for i in range(length-1, -1, -1):
            j = i - (len(b)-len(a))
            # print(i, j, carry, result)
            if j >=0 :
                tmp = int(a[j])+int(b[i])+carry
                carry = 0
            else:
                tmp = int(b[i])+carry
                carry = 0
            if tmp == 0:
                result = '0'+result
            elif tmp == 1:
                result = '1'+result
            elif tmp == 2:
                result = '0'+result
                carry = 1
            if tmp == 3:
                result = '1'+result
                carry = 1
        if carry == 1:
            result = str(carry)+result
            
        return result

            
# @lc code=end

