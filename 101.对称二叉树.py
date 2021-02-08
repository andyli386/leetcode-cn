#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(node1, node2):
            if not (node1 or node2):
                return True
            elif not (node1 and node2):
                return False

            if node1.val != node2.val:
                return False
            
            return check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root, root)
        

# @lc code=end

