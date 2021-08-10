#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -inf
        def getMax(root: TreeNode) -> int:
            if not root:
                return 0

            left = max(0, getMax(root.left))
            right = max(0, getMax(root.right))

            self.ans = max(self.ans, left+right+root.val)

            return max(left, right)+root.val
        getMax(root)
        return self.ans
# @lc code=end

