'''
Author: Vincent
Date: 2021-02-01 09:04:00
LastEditors: Vincent
LastEditTime: 2021-02-01 13:18:42
Description: file content
'''
#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
        print(res+str(out))
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ '.'*n for _ in range(n)]
        self.result = []

        self.backtrack(board, 0)

        return self.result

    def backtrack(self, board: List[List[str]], row: int):
        if row == len(board):
            self.result.append(board.copy())
            return

        for col in range(len(board[row])):
            if not self.isValid(board, row, col):
                continue

            board[row] = board[row][0:col]+'Q'+board[row][col+1:]
            self.backtrack(board, row+1)
            board[row] = board[row][0:col]+'.'+board[row][col+1:]


    def isValid(self, board, row, col):
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        for i, j in zip(range(row-1, -1, -1), range(col+1, len(board), 1)):
            if board[i][j] == 'Q':
                return False

        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

# @lc code=end

