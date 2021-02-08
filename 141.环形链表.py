'''
Author: Vincent
Date: 2021-02-02 11:43:28
LastEditors: Vincent
LastEditTime: 2021-02-02 12:04:53
Description: file content
'''
#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    count = 0
    def printIndent(self, out):
        res = ''
        for i in range(self.count):
            res += '*'
        print(res+str(out))
        
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head

        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
        
# @lc code=end

