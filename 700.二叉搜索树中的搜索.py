'''
Author: Vincent
Date: 2021-02-20 08:36:29
LastEditors: Vincent
LastEditTime: 2021-02-20 08:41:03
Description: file content
'''
#
# @lc app=leetcode.cn id=700 lang=python3
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def searchBST(self, root: TreeNode, val: int) -> TreeNode:
    #     if root == None: return None
    #     if root.val == val: return root
    #     return self.searchBST(root.left, val) or self.searchBST(root.right, val)
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root == None: return None
        if root.val == val: return root
        if root.val < val:
            return self.searchBST(root.right, val)
        if root.val > val:
            return self.searchBST(root.left, val)
            
# @lc code=end

