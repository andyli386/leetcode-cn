'''
Author: Vincent
Date: 2021-02-26 21:49:31
LastEditors: Vincent
LastEditTime: 2021-02-26 23:13:06
Description: file content
'''
#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self) -> None:
        self.successor = None

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left-1, right-1)

        return head
    
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        print(head)
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n-1)
        head.next.next = head
        head.next = self.successor
        
        return last
        
# @lc code=end

