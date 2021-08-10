'''
Author: Vincent
Date: 2021-02-20 09:05:05
LastEditors: Vincent
LastEditTime: 2021-02-20 09:29:00
Description: file content
'''
#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root == None: return None
        if root.val == key:
            if root.left == None: return root.right
            if root.right == None: return root.left

            minNode = self.getMin(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        return root

    def getMin(self, node):
        while node.left != None:
            node = node.left

        return node

        
# @lc code=end

