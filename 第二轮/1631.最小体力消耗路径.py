'''
Author: Vincent
Date: 2021-10-08 22:33:25
LastEditors: Vincent
LastEditTime: 2021-10-09 16:28:18
Description: file content
'''
#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
from typing import List
from queue import PriorityQueue

class Solution:

    def adj(self, matrix:List[List[int]], x:int, y:int) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        neighbors = []
        for i, j in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx = x + i
            ny = y + j
            if nx >= m or nx < 0 or ny >= n or ny < 0:
                continue
            neighbors.append([nx, ny])
        return neighbors

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        effortTo = [[inf for _ in range(n)] for _ in range(m)]
        effortTo[0][0] = 0
        
        pq = PriorityQueue()
        pq.put((0, 0, 0))

        while not pq.empty():

            curState = pq.get()

            curX = curState[1]
            curY = curState[2]
            curEffortFromStart = curState[0]

            if curX == m-1 and curY == n-1:
                return curEffortFromStart
            
            if (curEffortFromStart > effortTo[curX][curY]):
                continue


            for neighbor in self.adj(heights, curX, curY):
                nextX = neighbor[0]
                nextY = neighbor[1]
                effortToNextNode = max(effortTo[curX][curY], abs(heights[curX][curY]-heights[nextX][nextY]))

                if effortTo[nextX][nextY] > effortToNextNode:
                    effortTo[nextX][nextY] = effortToNextNode
                    pq.put((effortToNextNode, nextX, nextY))

        return -1

# @lc code=end

