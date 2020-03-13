'''
面试题68 - I. 二叉搜索树的最近公共祖先
难度简单
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]
示例 1:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。
示例 2:
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
说明:
	• 所有节点的值都是唯一的。
	• p、q 为不同节点且均存在于给定的二叉搜索树中。
注意：本题与主站 235 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

执行用时 :116 ms, 在所有 Python3 提交中击败了33.83%的用户
内存消耗 :17.8 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. empty tree: return None
# 2. 最近公共祖先节点可以为节点本身

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None:
            return None
        
        if p.val>q.val:
            big = p
            small = q
        else:
            big = q
            small = p

        if root.val>=small.val and root.val<=big.val:
            return root
        elif root.val>big.val:
            return self.lowestCommonAncestor(root.left, big,small)
        else: # root.val<small.val
            return self.lowestCommonAncestor(root.right,p,q)
