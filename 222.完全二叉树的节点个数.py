'''
Author: Vincent
Date: 2021-02-20 09:40:03
LastEditors: Vincent
LastEditTime: 2021-02-20 09:48:54
Description: file content
'''
#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        l = root; r = root
        hl = 0; hr = 0
        
        while l != None:
            l = l.left
            hl += 1

        while r != None:
            r = r.right
            hr += 1

        if hl == hr:
            return 2**hl-1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# @lc code=end

