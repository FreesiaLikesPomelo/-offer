'''
面试题28. 对称的二叉树
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
    1
   / \
  2   2
   \   \
   3    3
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：
输入：root = [1,2,2,null,3,null,3]
输出：false

执行用时 :32 ms, 在所有 Python3 提交中击败了97.65%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# test cases: recursively check
# 1. root==None return True
# 2. only one root node-> return True
# 3. [1,2,2,3,4,4,3]-> True
# 4. [1,2,2,None,3,None,3]->False
# 5. [1,2,2,3,None,None,3]->True
# 6. [1,2,2,3,None,None,None]->True
# 7. [1,0] -> False

class Solution:
    def is2TreeSymmetric(self, leftchild:TreeNode, rightchild:TreeNode)->bool:
        if leftchild==None:
            if rightchild==None:
                return True
            else:
                return False
        if rightchild==None and leftchild!=None:
            return False
        # none of these two nodes can be none
        if leftchild.val!=rightchild.val:
            return False
        # leftchild.val==rightchild.val
        if leftchild.left==None and leftchild.right==None:
            # leftchild is leaf node
            if rightchild.left==None and rightchild.right==None:
                # rightchild is leaf node
                return True
            else:
                # rightchild is not leaf node while leftchild is a leaf node
                return False
        else:
            if rightchild.left==None and rightchild.right==None:
                # leftchild is not leaf node while rightchild is a leaf node
                return False
            else:
                # both of them are not leaf nodes
                firstAns = self.is2TreeSymmetric(leftchild.left, rightchild.right)
                seconAns = self.is2TreeSymmetric(leftchild.right, rightchild.left)
                if firstAns and seconAns:
                    return True
                else:
                    return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        if root.left==None:
            if root.right==None:
                return True
            else:
                return False
        if root.right==None and root.left!=None:
            return False
        
        child = False
        if root.left.val==root.right.val:
            child = True
        grandchild = self.is2TreeSymmetric(root.left, root.right)
        if grandchild and child:
            return True
        else:
            return False
