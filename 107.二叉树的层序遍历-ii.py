#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
            
        allNodes = []
        allNodes.append([root])
        for levelNodes in allNodes:
            nodes = []
            for node in levelNodes:
                if  node.left and node.right:
                    nodes.extend([node.left, node.right])
                elif not node.left and node.right:
                    nodes.extend([node.right])
                elif node.left and not node.right:
                    nodes.extend([node.left])
            if nodes:
                allNodes.append(nodes)
        
        results = []
        for levelNodes in allNodes[::-1]:
            level = []
            for node in levelNodes:
                level.append(node.val)

            results.append(level)

        return results

# @lc code=end

