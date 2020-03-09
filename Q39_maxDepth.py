'''
面试题55 - I. 二叉树的深度
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
例如：
给定二叉树 [3,9,20,null,null,15,7]，
    3
   / \
  9  20
    /  \
   15   7
返回它的最大深度 3 。
提示：
节点总数 <= 10000

执行用时 :52 ms, 在所有 Python3 提交中击败了57.39%的用户
内存消耗 :14.9 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# test cases:
# 1. empty tree: return 0
# 2. only one root node: return 1
# 3. function test

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            lDep = 0
            rDep = 0
            if root.left:
                lDep = self.maxDepth(root.left)
            if root.right:
                rDep = self.maxDepth(root.right)
            if lDep>rDep:
                return lDep+1
            else:
                return rDep+1
