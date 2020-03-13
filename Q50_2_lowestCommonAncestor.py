'''
面试题68 - II. 二叉树的最近公共祖先
难度简单
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:
	• 所有节点的值都是唯一的。
	• p、q 为不同节点且均存在于给定的二叉树中。
注意：本题与主站 236 题相同：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
来自 <https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/> 

执行用时 :104 ms, 在所有 Python3 提交中击败了38.79%的用户
内存消耗 :4.6 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ppath = []
        self.qpath = []

    def find2path(self, root:TreeNode, temp:List[TreeNode], findFlag: int, p: TreeNode, q:TreeNode)->TreeNode:
        # temp is the list contains the path now for the current visit node 
        # store path to p in path[0], path to q in path[1]
        
        if findFlag==2:
            return

        if root==None:
            dummy = 0
            temp.append(dummy)
            return None
        #print("root:", root.val)
        temp.append(root)
        if root==p:
            self.ppath = temp.copy()
            #print("p-path_after it:")
            #for i in range(len(self.ppath)):
            #    print(self.ppath[i].val)
            findFlag+=1
        if root==q:
            self.qpath = temp.copy()
            #print("q-path_after it:")
            #for i in range(len(self.qpath)):
            #    print(self.qpath[i].val)
            findFlag+=1
        
        if root.left==None and root.right==None: # leafNode
            #if root!=p and root!=q:
            #    temp.pop() # pop non target node
            return
        
        self.find2path(root.left,temp,findFlag,p,q)
        x = temp.pop()
        #print("back to the root node, pop left:",x.val)
        self.find2path(root.right,temp,findFlag,p,q)
        x = temp.pop()
        #print("back to the root node, pop right:",x.val)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if p or q is root, then the lowest common ancestor mus be itself.
        if root==p or root==q:
            return root 
        # find two paths to the given two nodes. root->left->right
        currentPath = []
        findFlag = 0
        
        self.find2path(root,currentPath,findFlag,p,q)

        idx = 0
        len1 = len(self.ppath)
        len2 = len(self.qpath)
        
        while idx<len1 and idx<len2 and self.ppath[idx].val==self.qpath[idx].val:
            # print("comparing: ",self.ppath[idx].val,self.qpath[idx].val,idx)
            idx+=1
        #print("idx: ",idx, "common Node:",self.ppath[idx-1].val)
        return self.ppath[idx-1]

        

