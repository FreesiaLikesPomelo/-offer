# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# right-root-left count k
# test cases:
# 1. empty tree: return None
# 2. K>tree elements: return None

# 执行用时 :64 ms, 在所有 Python3 提交中击败了65.85%的用户
# 内存消耗 :17.6 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def __init__(self):
        self.ans = -100
        self.count = 0

    def treeList(self, root:TreeNode,k):
        if self.count<=k:
            if root==None:
                return 

            if root.left==None and root.right==None:
                self.count+=1
                if self.count==k:
                    self.ans = root.val
                #print(root.val,self.count)
                return 
        
            self.treeList(root.right,k)
            self.count+=1
            if self.count==k:
                self.ans = root.val
            # print(root.val,self.count)
            self.treeList(root.left,k)
            return 
        else:
            return

    def kthLargest(self, root: TreeNode, k: int) -> int:
        if root==None:
            return None
        # if k > tree's length
        self.treeList(root,k)
        return self.ans
    
# left-root-right count k
# test cases:
# 1. empty tree: return None
# 2. K>tree elements: return None
'''
# 执行用时 :68 ms, 在所有 Python3 提交中击败了51.10%的用户
# 内存消耗 :17.3 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def treeList(self, root:TreeNode):
        if root==None:
            return []

        if root.left==None and root.right==None:
            return [root]
        
        left = self.treeList(root.left)
        right = self.treeList(root.right)
        return left+[root]+right

    def kthLargest(self, root: TreeNode, k: int) -> int:
        if root==None:
            return None
        # if k > tree's length
        treeList = self.treeList(root)
        if k>len(treeList):
            return None
        else:
            res = treeList[-k].val
            return res
'''
