'''
Author: Vincent
Date: 2021-02-28 22:18:43
LastEditors: Vincent
LastEditTime: 2021-03-01 00:14:08
Description: file content
'''
#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isValid(board, row, col, c):
            for i in range(9):
                if board[row][i] == c: 
                    return False
                if board[i][col] == c: 
                    return False

                if board[(row//3)*3+i//3][(col//3)*3+i%3] == c: 
                    return False

            return True

        def backtrack(board, row, col):
            m = 9; n = 9
            if col == n:
                return backtrack(board, row+1, 0)

            if row == m:
                return True

            if board[row][col] != '.':
                return backtrack(board, row, col+1)

            for ch in [str(i) for i in range(1, 10)]:
                if (not isValid(board, row, col, ch)):
                    continue
                board[row][col] = ch

                if backtrack(board, row, col+1):
                    return True

                board[row][col] = '.'

            return False
        
        backtrack(board, 0, 0)
# class Solution:
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: void Do not return anything, modify board in-place instead.
#         """
#         def check(x, y, s):
#             for i in range(9):
#                 if board[i][y] == s or board[x][i] == s:
#                     return False
#             for i in [0, 1, 2]:
#                 for j in [0, 1, 2]:
#                     if board[x//3*3+i][y//3*3+j] == s:
#                         return False
#             return True
        
#         def bt(cur):
#             if cur == 81:
#                 return True
#             x, y = cur // 9, cur % 9
#             if board[x][y] != '.':
#                 return bt(cur + 1)
#             for i in range(1, 10):
#                 s = str(i)
#                 if check(x, y, s):
#                     board[x][y] = s
#                     if bt(cur + 1):
#                         return True
#                     board[x][y] = '.'
#             return False
        
#         bt(0)

# @lc code=end

