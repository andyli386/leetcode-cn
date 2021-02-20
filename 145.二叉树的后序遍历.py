'''
Author: Vincent
Date: 2021-02-20 11:05:35
LastEditors: Vincent
LastEditTime: 2021-02-20 11:07:57
Description: file content
'''
#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        return self.postTrave(root, result)

    def postTrave(self, root, result):
        if root == None: return result
        result = self.postTrave(root.left, result)
        result = self.postTrave(root.right, result )
        result.append(root.val)
        
        return result
# @lc code=end

