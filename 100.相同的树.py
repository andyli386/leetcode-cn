#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # if p == None and q == None:
        #     return True
        # elif (p == None and q != None) or (q == None and  p != None):
        #     return False

        # if p.val != q.val:
        #     return False
        # else:
        #     result = self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # return result
        return str(p) == str(q)
# @lc code=end

