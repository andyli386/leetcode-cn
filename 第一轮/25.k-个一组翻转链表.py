'''
Author: Vincent
Date: 2021-02-27 00:53:04
LastEditors: Vincent
LastEditTime: 2021-02-27 01:19:17
Description: file content
'''
#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return head
        a = b = head
        for i in range(k):
            if b == None: return head
            b = b.next

        newHead = self.reverseList(a, b)
        a.next = self.reverseKGroup(b, k)

        return newHead

    def reverseList(self, head: ListNode, last: ListNode) -> ListNode:
        pre = None; cur = head; next = None
        while cur != last:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre
# @lc code=end

