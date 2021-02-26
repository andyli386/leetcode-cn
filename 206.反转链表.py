'''
Author: Vincent
Date: 2021-02-25 19:46:09
LastEditors: Vincent
LastEditTime: 2021-02-27 01:12:39
Description: file content
'''
#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if head == None or head.next == None:
    #         return head
        
    #     last = self.reverseList(head.next)
    #     head.next.next = head
    #     head.next = None
    #     return last
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None; cur = head; next = None
        while cur != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        
        return pre

# @lc code=end

