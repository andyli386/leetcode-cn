#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # count = 0
    # def printIndent(self, out):
    #     res = ''
    #     for i in range(self.count):
    #         res += '-'
    #     print(res+str(out))

    # def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    #     if not (preorder and inorder):
    #         return None
        
    #     # self.count += 1
    #     # self.printIndent('preorder '+str(preorder))
    #     # self.printIndent('inorder '+str(inorder))

    #     root = TreeNode(preorder[0])

    #     root.left = self.buildTree(
    #         # inorder.index(preorder[0]) 根节点在inorder中位置
    #         preorder = preorder[1: inorder.index(preorder[0])+1],
    #         inorder=inorder[:inorder.index(preorder[0])]
    #     )
    #     # self.printIndent('left '+str(root.left))

    #     root.right = self.buildTree(
    #         preorder = preorder[inorder.index(preorder[0])+1:],
    #         inorder=inorder[inorder.index(preorder[0])+1:]
    #     )

    #     # self.printIndent('right '+str(root.right))
    #     # self.count -= 1
        
    #     return root
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None          

        x = preorder.pop(0)
        root = TreeNode(x)
        index = inorder.index(x)

        root.left = self.buildTree(preorder[:index], inorder[:index])
        root.right = self.buildTree(preorder[index:], inorder[index+1:])

        return root
        
# @lc code=end
