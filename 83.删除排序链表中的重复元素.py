#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return 
            
        q = head 
        p = q.next
        while p:
            if p.val == q.val:
                q.next = p.next
                p = p.next
            else:
                p = p.next
                q = q.next
        
        return head


# @lc code=end

