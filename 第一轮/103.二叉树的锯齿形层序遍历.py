'''
Author: Vincent
Date: 2021-02-20 12:42:58
LastEditors: Vincent
LastEditTime: 2021-02-20 14:40:21
Description: file content
'''
#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode [val: {self.val}, left: {self.left}, right: {self.right}]'
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if root == None: return results

        queues = []
        queues.append([root])

        level = 0

        while queues:
            result = []
            queue = []
            firstlevel = queues.pop(0)
            while firstlevel:
                if level % 2 == 0:
                    node = firstlevel.pop(0)
                else:
                    node = firstlevel.pop(-1)
                
                if node == None: continue

                if level % 2 == 0:
                    queue.extend([node.left, node.right])
                else:
                    queue.insert(0, node.right)
                    queue.insert(0, node.left)
                    
                result.append(node.val)

            if queue:
                queues.append(queue)
            if result:
                results.append(result)
            
            level += 1

        return results

# @lc code=end


def buildTree(result):
    if not result:
        return None
    r = result.pop(0)
    if r == None:
        return None
    print(f'result: {result}')
    root = TreeNode(int(r))
    root.left = buildTree(result)
    root.right = buildTree(result)

    return root
if __name__ == '__main__':
    tree = buildTree([3,9,20,None,None,15,7])
    print(tree)