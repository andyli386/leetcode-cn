'''
Author: Vincent
Date: 2021-02-02 13:06:21
LastEditors: Vincent
LastEditTime: 2021-02-02 13:07:19
Description: file content
'''
#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        return slow
        
# @lc code=end

