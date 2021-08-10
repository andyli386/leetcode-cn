'''
Author: Vincent
Date: 2021-02-02 12:56:28
LastEditors: Vincent
LastEditTime: 2021-02-02 13:03:18
Description: file content
'''
#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        hasCycle = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                hasCycle = True
                break

        if not hasCycle:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow


# @lc code=end

