'''
Author: Vincent
Date: 2021-02-23 19:56:01
LastEditors: Vincent
LastEditTime: 2021-02-25 09:15:24
Description: file content
'''
#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    #     self.left = head
    #     return self.traverse(head)

    # def traverse(self, right):
    #     if right == None: return True
    #     res = self.traverse(right.next)
    #     res = res and (right.val == self.left.val)
    #     self.left = self.left.next

    #     return res
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        if fast != None:
            slow = slow.next

        left = head
        right = self.reverse(slow)

        while right != None:
            if left.val != right.val:
                return False

            left = left.next
            right = right.next
        
        return True

    def reverse(self, head):
        pre = None; cur = head
        while cur != None:
            next = cur.next
            cur.next = pre

            pre = cur
            cur = next

        return pre

# @lc code=end

