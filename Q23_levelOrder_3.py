# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# first row -> queue -> import queue
# second row -> stack -> List[TreeNode]
# two stacks were used to maintain the sequences.

# test cases:
# 1. empty root node;
# 2. only one node: return [[root.val]];
# 3. normal tree.

import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root==None:
            return []
        else:
            result = []
            if root.left==None and root.right==None:
                temp = []
                temp.append(root.val)
                result.append(temp)
                return result
            else:
                q = queue.Queue()
                q.put(root)
                stk = []
                while q.empty()==False or stk!=[]:
                    # when both of them are not empty, continue the circulation
                    rtemp = []
                    if q.empty()==False:
                        # if q is not empty
                        while q.empty()==False:
                            tempNode = q.get()
                            if tempNode.left!=None:
                                stk.append(tempNode.left) 
                            if tempNode.right!=None:
                                stk.append(tempNode.right)
                            rtemp.append(tempNode.val)
                        result.append(rtemp)
                        rtemp = []
                    if stk!=[]:
                        # if stk is not empty
                        tempStk = []
                        while stk!=[]:
                            tempNode = stk.pop()
                            rtemp.append(tempNode.val)
                            tempStk.append(tempNode)
                        result.append(rtemp)
                        rtemp = []
                        while tempStk!=[]:
                            tempNode = tempStk.pop()
                            if tempNode.left!=None:
                                q.put(tempNode.left)
                            if tempNode.right!=None:
                                q.put(tempNode.right)
                return result
                           
