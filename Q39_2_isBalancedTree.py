'''
面试题55 - II. 平衡二叉树
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
示例 1:
给定二叉树 [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
返回 true 。
示例 2:
给定二叉树 [1,2,2,3,3,null,null,4,4]
       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。
限制：
1 <= 树的结点个数 <= 10000
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#执行用时 :60 ms, 在所有 Python3 提交中击败了80.29%的用户
#内存消耗 :17.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        elif root.left==None and root.right==None:
            return True
        else:
            result,temp = self.travelTree(root,0)
            return result
            
    def travelTree(self, root: TreeNode, depth)->List[TreeNode]: # and int depth
        if root==None:
            return True,depth
        elif root.left==None and root.right==None: # leaf node 
            depth+=1
            #print("LeafNode:",root.val,"depth",depth)
            return True,depth
        else:
            templ,left = self.travelTree(root.left,depth)
            tempr,right = self.travelTree(root.right,depth)
            #print("root:",root.val,"left",left,"right",right)
            if templ==False or tempr==False:
                return False,-1
            if left>right:
                depth = left+1
                dif = left-right
            else:
                depth = right+1
                dif = right-left
            if dif<-1 or dif>1:
                return False, depth
            else:
                return True,depth

'''
# 执行用时 :60 ms, 在所有 Python3 提交中击败了80.29%的用户
# 内存消耗 :17.1 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root==None:
            return True
        elif root.left==None and root.right==None:
            return True
        else:
            lDep = self.treeDepth(root.left)
            rDep = self.treeDepth(root.right)
            temp = lDep-rDep
            if temp<-1 or temp>1:
                return False
            return self.isBalanced(root.left) and self.isBalanced(root.right)

    def treeDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        elif root.left==None and root.right==None:
            return 1
        else:
            lDep = 0
            rDep = 0
            if root.left:
                lDep = self.treeDepth(root.left)
            if root.right:
                rDep = self.treeDepth(root.right)
            if lDep>rDep:
                return lDep+1
            else:
                return rDep+1
'''

