'''
Author: Vincent
Date: 2021-10-07 15:56:31
LastEditors: Vincent
LastEditTime: 2021-10-07 16:26:49
Description: file content
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = ['.'*n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        if row == len(board):
            self.res.append(copy.deepcopy(board))
            return 
        n = len(board[row])
        for col in range(n):
            if not self.isValid(board, row, col):
                continue
            board[row] = board[row][0:col]+'Q'+board[row][col+1:]
            self.backtrack(board, row+1)
            board[row] = board[row][0:col]+'.'+board[row][col+1:]

    def isValid(self, board, row, col):
        # 列
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False

        # 右上角
        for i, j in zip(range(row-1, -1, -1), range(col+1, len(board[row]))):
            if board[i][j] == 'Q':
                return False
        
        # 左上角
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True
# @lc code=end

