# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# using two ques to represent
# test cases:
# 1. empty root
# 2. only one node : return [[x]]
# 3. normal tree

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
                q1 = queue.Queue()
                q2 = queue.Queue()
                q1.put(root)
                while q1.empty()==False or q2.empty()==False: 
                    # when both of them are not empty, continue the circulation
                    rtemp = []
                    if q1.empty() == False: # q1 has element in it
                        while q1.empty()==False: 
                            temp = q1.get()
                            if temp.left!=None:
                                q2.put(temp.left)
                            if temp.right!=None:
                                q2.put(temp.right)
                            rtemp.append(temp.val)
                        result.append(rtemp)
                        rtemp = []
                    if q2.empty() == False: # q2 has element in it
                        while q2.empty()==False:
                            temp = q2.get()
                            if temp.left!=None:
                                q1.put(temp.left)
                            if temp.right!=None:
                                q1.put(temp.right)
                            rtemp.append(temp.val)
                        result.append(rtemp)
                        rtemp = []
                return result




                
