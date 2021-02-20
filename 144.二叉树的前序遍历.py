'''
Author: Vincent
Date: 2021-02-20 10:42:59
LastEditors: Vincent
LastEditTime: 2021-02-20 11:04:45
Description: file content
'''
#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        return self.preTrave(root, result)

    def preTrave(self, root, result):
        if root == None: return result
        result.append(root.val)
        result = self.preTrave(root.left, result)
        result = self.preTrave(root.right, result)
        return result

# @lc code=end

