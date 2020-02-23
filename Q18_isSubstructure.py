# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
test case: 
1. tree1-None-> return false,
2. tree2-None-> return true,
3. tree2 have more then 2 layers
'''

class Solution(object):
    def isAHasBRoot(self, A, B):
        '''
        :type A: TreeNode (cannot be None)
        :type B: TreeNode (cannot be None)
        :rtype: bool
        traverse the tree A, to find if the root of B is contained in A
        '''
        result = False
        if A!=None and B!=None:
            if A.val==B.val:
                # now check the substructure
                result = self.isAHasB(A,B)
            if result==False:
                result = self.isAHasBRoot(A.left,B)
            if result==False:
                result = self.isAHasBRoot(A.right,B)
        return result
        
    def isAHasB(self, A, B):
        '''
        :type A: TreeNode (cannot be None)
        :type B: TreeNode (cannot be None)
        :rtype: bool
        to check if A contains B
        '''
        if B==None:
            return True
        if A==None:
            return False
        if A.val!=B.val:
            return False

        result1 = self.isAHasB(A.left,B.left)
        result2 = self.isAHasB(A.right,B.right)
        return result1&result2


    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        if A==None:
            return False
        elif B==None:
            return False
        else:
            return self.isAHasBRoot(A,B)
