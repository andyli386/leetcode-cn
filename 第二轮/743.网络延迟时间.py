'''
Author: Vincent
Date: 2021-10-08 20:22:31
LastEditors: Vincent
LastEditTime: 2021-10-08 21:30:03
Description: file content
'''
#
# @lc app=leetcode.cn id=743 lang=python3
#
# [743] 网络延迟时间
#

# @lc code=start
from typing import List
from queue import PriorityQueue

class State:
    def __init__(self, id:int, distFromStart ) -> None:
        self.id = id
        self.distFromStart = distFromStart
    
    def __f(self, x):
        return x % 16

    def __lt__(self, obj):
        """self < obj."""
        return self.__f(self.distFromStart) < self.__f(obj.distFromStart)

    def __le__(self, obj):
        """self <= obj."""
        return self.__f(self.distFromStart) <= self.__f(obj.distFromStart)

    def __eq__(self, obj):
        """self == obj."""
        return self.__f(self.distFromStart) == self.__f(obj.distFromStart)

    def __ne__(self, obj):
        """self != obj."""
        return self.__f(self.distFromStart) != self.__f(obj.distFromStart)

    def __gt__(self, obj):
        """self > obj."""
        return self.__f(self.distFromStart) > self.__f(obj.distFromStart)

    def __ge__(self, obj):
        """self >= obj."""
        return self.__f(self.distFromStart) >= self.__f(obj.distFromStart)

class Solution:
    def dijkstra(self, start:int, graph:List[List[int]]) -> int:
        distTo = [inf for _ in range(len(graph))]
        distTo[start] = 0

        pq = PriorityQueue()
        pq.put(State(start, 0))

        while not pq.empty():
            curState = pq.get()
            curNodeId = curState.id
            curDistFromStart = curState.distFromStart

            if curDistFromStart > distTo[curNodeId]:
                continue

            #print(curNodeId)
            for neighbor in graph[curNodeId]:
                # print(neighbor)
                if neighbor:
                    nextNodeID = neighbor[0]
                    distToNextNode = distTo[curNodeId] + neighbor[1]
                    if distTo[nextNodeID] > distToNextNode:
                        distTo[nextNodeID] = distToNextNode
                        pq.put(State(nextNodeID, distToNextNode))
        
        return distTo

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]
        for edge in times:
            src = edge[0]
            to = edge[1]
            weight = edge[2]
            graph[src].append([to, weight])
        
        # print(graph)
        distTo = self.dijkstra(k, graph)
        # print(distTo)
        res = 0
        for i in range(1, len(distTo)):
            if distTo[i] == inf:
                return -1
            res = max(res, distTo[i])

        return res

# @lc code=end

