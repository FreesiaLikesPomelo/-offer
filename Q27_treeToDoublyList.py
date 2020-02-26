"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

"""
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/

执行用时 :40 ms, 在所有 Python3 提交中击败了78.57%的用户
内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
"""

class Solution:
    def midTravers(self, root:'Node')->'List':
        if root==None:
            return []
        left = self.midTravers(root.left)
        right = self.midTravers(root.right)
        return left+[root]+right
        
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root==None:
            return None
        
        if root.left==None and root.right==None: # only one node
            root.left = root
            root.right = root
            return root
        
        # 中序遍历 结点存进队列
        midList = self.midTravers(root)
        for i in range(len(midList)):
            if i==0:
                midList[0].left = midList[-1]
                midList[0].right = midList[1]
            elif i!=len(midList)-1:# not the last one
                midList[i].left = midList[i-1]
                midList[i].right = midList[i+1]
            else:
                midList[i].left = midList[i-1]
                midList[i].right = midList[0]
        
        return midList[0]
