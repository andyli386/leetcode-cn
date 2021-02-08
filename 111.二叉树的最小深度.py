'''
Author: Vincent
Date: 2021-02-02 08:46:19
LastEditors: Vincent
LastEditTime: 2021-02-02 08:55:03
Description: file content
'''
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None: return 0

        q = []
        q.append(root)

        depth = 1

        while len(q) :
            for i in range(len(q)):
                current = q[0]
                q = q[1:]
                if current.left == None and current.right == None:
                    return depth
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            depth += 1
        return depth
# @lc code=end

