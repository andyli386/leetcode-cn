'''
Author: Vincent
Date: 2021-10-07 17:00:23
LastEditors: Vincent
LastEditTime: 2021-10-07 17:10:44
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
        if root is None:
            return 0
        q = [root]
        depth = 1

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q[0]
                q = q[1:]
                if cur.left == None and cur.right == None:
                    return depth
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)

            depth += 1

        return depth
# @lc code=end

