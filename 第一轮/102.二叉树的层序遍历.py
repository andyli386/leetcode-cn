'''
Author: Vincent
Date: 2021-02-20 11:17:17
LastEditors: Vincent
LastEditTime: 2021-02-20 12:41:28
Description: file content
'''
#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if root == None: return results

        queues = []
        queues.append([root])

        while queues:
            result = []
            queue = []
            firstlevel = queues.pop(0)
            while firstlevel:
                node = firstlevel.pop(0)
                
                if node == None: continue

                queue.extend([node.left, node.right])
                result.append(node.val)

            if queue:
                queues.append(queue)
            if result:
                results.append(result)
            
        return results

# @lc code=end

