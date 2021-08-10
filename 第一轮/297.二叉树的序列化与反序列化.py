'''
Author: Vincent
Date: 2021-02-20 13:35:12
LastEditors: Vincent
LastEditTime: 2021-02-20 14:28:04
Description: file content
'''
#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = ''
        result = self.seria(root, result)
        return result
        
    def seria(self, root, result):
        if root == None:
            result += '#'
            result += ','
            return result
        
        result += str(root.val)
        result += ','

        result = self.seria(root.left, result)
        result = self.seria(root.right, result)

        return result
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        result = data.split(',')

        return self.deseria(result)

    def deseria(self, result):
        if not result:
            return None
        r = result.pop(0)
        if r == '#': return None

        root = TreeNode(int(r))
        root.left = self.deseria(result)
        root.right = self.deseria(result)

        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

    
