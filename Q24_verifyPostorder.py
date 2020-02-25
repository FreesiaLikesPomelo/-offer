# 后序： 左-右-根
# 二叉搜索树： 左＜根＜右
# test cases:
# 1. empty list: return None/false
# 2. only one node: return true
# 3. normal trees: function test

'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
参考以下这颗二叉搜索树：
     5
    / \
   2   6
  / \
 1   3
示例 1：
输入: [1,6,3,2,5]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时 :72 ms, 在所有 Python3 提交中击败了24.54%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

class Solution:
    def isTreeQualifyRoot(self, treelist: List[int], root: int, flag: int)-> bool:
        result = True
        if flag==0: 
            # left tree need to be smaller than the root 
            for i in range(len(treelist)):
                if root<treelist[i]:
                    return False
        if flag==1:
            # right tree need to be bigger than the root
            for i in range(len(treelist)):
                if root>treelist[i]:
                    return False
        return result 

    def verifyPostorder(self, postorder):
        if postorder==[]:
            return True
        elif len(postorder)<=2:
            return True
        else:
            rResult = True
            lResult = True
            root = postorder.pop() # get the root
            #print("root:",root)
            idx = 0
            for i in range(len(postorder)):
                if postorder[i]>root: # find the idx of right subtree
                    idx = i
                    break 
                if i==len(postorder)-1: # only have left-tree
                    if self.isTreeQualifyRoot(postorder,root,0)==False:
                        return False
                    lResult = self.verifyPostorder(postorder)
                    return lResult
            if idx==0:# only have right-tree
                if self.isTreeQualifyRoot(postorder,root,1)==False:
                    return False
                rResult = self.verifyPostorder(postorder)
                return rResult	
            if idx>0 and idx<len(postorder):# have two sub-tree
                # when it's in the middl, there are two sub-trees
                if self.isTreeQualifyRoot(postorder[:idx],root,0)==False:
                    return False
                if self.isTreeQualifyRoot(postorder[idx:],root,1)==False:
                    return False
                lResult = self.verifyPostorder(postorder[:idx])
                #print("postorder[:idx]:",postorder[:idx],"rResult:",rResult)
                rResult = self.verifyPostorder(postorder[idx:])
                #print("postorder[idx:]:",postorder[idx:],"lResult:",lResult)
                result = False
                if rResult and lResult:
                    result = True
                return result
