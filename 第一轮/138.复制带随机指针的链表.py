#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return 

        dic = {}
        dic[None] = None

        cur = head
        while cur:
            if cur not in dic:
                dic[cur] = Node(cur.val)
            
            if cur.random not in dic:
                dic[cur.random] = Node(cur.random.val)
            dic[cur].random = dic[cur.random]

            if cur.next not in dic:
                dic[cur.next] = Node(cur.next.val)
            dic[cur].next = dic[cur.next]

            cur = cur.next

        return dic[head]
        
# @lc code=end

