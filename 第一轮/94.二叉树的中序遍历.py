'''
Author: Vincent
Date: 2021-02-20 11:08:37
LastEditors: Vincent
LastEditTime: 2021-02-20 11:16:37
Description: file content
'''
#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        return self.inTrave(root, result)

    def inTrave(self, root, result):
        if root == None: return result
        result = self.inTrave(root.left, result)
        result.append(root.val)
        result = self.inTrave(root.right, result)
        return result 
# @lc code=end

