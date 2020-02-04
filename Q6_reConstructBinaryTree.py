# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#  preversal traversal:root nodes are always in the left part.
#  inorder traversal: left trees are always in the left part.
#  so we can use the preversal traversal to determine the root node.
#  and then we can use the inorder traversal to determin the left/right tree.
#  we can solve this problem recursively.
#  Notice: since there is no repeated numbers in the preversal traversal list, 
#so we can use list.index[value] to get the position of the root node in inorder traversal,
# to splite it into left tree and right tree.
'''
test case (including boundary condition):
1. normal binary tree.
2. NULL(None)
3. only one node
'''
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None
        elif len(pre)==1:
            return TreeNode(pre[0])
        else:
            root = TreeNode(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:tin.index(pre[0])+1],tin[0:tin.index(pre[0])])
            root.right = self.reConstructBinaryTree(pre[tin.index(pre[0])+1:],tin[tin.index(pre[0])+1:])
            return root
