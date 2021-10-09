'''
Author: Vincent
Date: 2021-10-09 17:16:14
LastEditors: Vincent
LastEditTime: 2021-10-10 01:01:00
Description: file content
'''
#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#

# @lc code=start
from queue import PriorityQueue
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            source = edges[i][0]
            target = edges[i][1]
            weight = succProb[i]
            graph[source].append([weight, target])
            graph[target].append([weight, source])

        return self.dijkstra(start, end, graph)

    def dijkstra(self, start, end, graph):
        probTo = [-1 for _ in range(len(graph))]
        probTo[start] = 1

        pq = PriorityQueue()
        pq.put((-1.0, start))

        while not pq.empty():
            curState = pq.get()
            curNodeId = curState[1]
            curProbFromStart = -1*curState[0]
            if curNodeId == end:
                return curProbFromStart
            
            if curProbFromStart < probTo[curNodeId]:
                continue
            
            for neighbor in graph[curNodeId]:
                nextNodeId = neighbor[1]
                probToNextNode = probTo[curNodeId] * neighbor[0]
                if probTo[nextNodeId] < probToNextNode:
                    probTo[nextNodeId] = probToNextNode
                    pq.put([-1*probToNextNode, nextNodeId])
        return 0.0


# @lc code=end

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
s = Solution()
result = s.maxProbability(n, edges, succProb, start, end)
#print(result)