# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
test case:
1. Normal tree--function test
2. input empty tree-- return None
3. input only one node
4. one of the sub-tree is empty tree--robust test
'''

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root==None:
            return None
        
        if root.left==None:
            if root.right==None: # only one node contained in the tree
                return root
            else: # left tree is none, but right tree is not
                root.left = self.mirrorTree(root.right)
                root.right = None
        else:
            if root.right==None: # right tree is none, but left tree is not
                root.right = self.mirrorTree(root.left)
                root.left = None
            else: # both of the subtrees are not empty tree
                temp = root.right
                root.right = self.mirrorTree(root.left)
                root.left = self.mirrorTree(temp)
        return root
