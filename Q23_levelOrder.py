# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# test cases:
# 1. empty tree: return None
# 2. normal tree: function test-> two subtree/only one subtree
# 3. tree with only one node

# using que

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        else: 
            result = []
            que = []
            if root.left==None and root.right==None:
                result.append(root.val)
                return result
            else:
            # for normal tree
            # using queue to store them
                que.append(root) # store the root node 
                i = 0
                while i<len(que):
                    if que[i].left!= None:
                        que.append(que[i].left)
                    if que[i].right!= None:
                        que.append(que[i].right)
                    result.append(que[i].val)
                    i+=1
                return result



                
