'''
面试题07. 重建二叉树
输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：
0 <= 节点个数 <= 5000
注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# test case:
# input: [] return None
# input: [root] return root
# input: [root,left] 
# input: [root,right]
# input: [root, left, right] 
# [1,2,4,5,3,7] & [4,2,5,1,3,7]

# 执行用时 :208 ms, 在所有 Python3 提交中击败了43.42%的用户
# 内存消耗 :87.5 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def _buildTree(self, preorder: List[int], inorder: List[int])->TreeNode:
        if preorder==[]:
            return None
        if len(preorder)==1:
            root = TreeNode(preorder[0])
            return root
        
        root = TreeNode(preorder[0]) # root node
        rootIdx = inorder.index(preorder[0])
        leftLength = len(inorder[:rootIdx])
        root.left = self._buildTree(preorder[1:leftLength+1],inorder[:rootIdx])
        root.right = self._buildTree(preorder[leftLength+1:],inorder[rootIdx+1:])

        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder)==0:
            return
        if len(preorder)==1:
            root = TreeNode(preorder[0])
            return root
        
        root = self._buildTree(preorder, inorder)

        return root        
