'''
Author: your name
Date: 2020-11-29 18:05:28
LastEditTime: 2020-11-29 21:45:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /test/Users/vincent/Work/projects/onlineproj/leetcode-cn/21.合并两个有序链表.py
'''

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        i = l1
        j = l2
        s = ListNode()
        t = s
        while (i is not None) or (j is not None):
            if (i is not None) and (j is not None):
                if i.val < j.val:
                    t.next = i
                    t = t.next
                    i = i.next
                else:
                    t.next = j
                    t = t.next
                    j = j.next
            elif i is None:
                t.next = j
                break
            elif j is None:
                t.next = i
                break
        return s.next

# @lc code=end
