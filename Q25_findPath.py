# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
示例:
给定如下二叉树，以及目标和 sum = 22，
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:
[
   [5,4,11,2],
   [5,8,4,5]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时 :48 ms, 在所有 Python3 提交中击败了82.51%的用户
内存消耗 :14.8 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root==None:
            return []
        temp = []
        if root.left==None and root.right==None: # leaf
            if root.val==sum:
                return [[root.val]]
            else: 
                return []
        else: # other nodes
            left = self.pathSum(root.left, sum-root.val)
            right = self.pathSum(root.right, sum-root.val)
            for item in left+right:
                temp.append([root.val]+item)
            return temp
