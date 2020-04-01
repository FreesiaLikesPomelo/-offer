'''
面试题37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。
示例: 
你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 执行用时 :240 ms, 在所有 Python3 提交中击败了22.75%的用户
# 内存消耗 :31 MB, 在所有 Python3 提交中击败了100.00%的用户
class Codec:
    def __init__(self):
        self.tree = []
        self.temp = []
        self.flag = 1 # non-None element appears again add self.temp to self.tree

    def traByLayer(self, tree: List[TreeNode]):
        if tree==[]:
            return
        else:
            temp = tree.pop(0)
            if temp!=None:
                self.tree+=self.temp
                self.temp = []
                self.tree.append(temp.val)
                tree.append(temp.left)
                tree.append(temp.right)
            else:
                self.temp.append(None)
                
            #print("trabylary",self.tree)
            self.traByLayer(tree)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return ''
        tree = [root]
        self.traByLayer(tree)
        print(str(self.tree))
        return str(self.tree)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        #data = '[1, 2, 3, 1, 3, 2, 4]'
        if data=='':
            return None
        start = 0
        end = 0
        tree = []
        for i in range(len(data)):
            if data[i]==',' or data[i]==']':
                start = end+1
                end = i
                if data[start:end]!=' None':
                    #print(start,end,data[start:end])
                    tree.append(int(data[start:end]))
                else:
                    tree.append(None)
        #print("Tree",tree,"then build the Tree")
        root = TreeNode(tree.pop(0))
        self.buildTreeByList([root],tree)
        return root

    def buildTreeByList(self,r:List[TreeNode], data: List[int]):
        if r==[] or data==[]:
            return
        root = r.pop(0)
    
        datalen = len(data)
        if datalen==0:
            return
        elif datalen<=2:
            #print("root",root.val,"tree",data,"datalen",datalen)
            temp = data.pop(0)
            if temp!=None:
                root.left = TreeNode(temp)
                r.append(root.left)
            if data!=[]:
                temp = data.pop(0)
                if temp!=None:
                    root.right = TreeNode(temp)
                    r.append(root.right)
            return
        else:
            #print("root",root.val,"tree",data,"datalen",datalen)
            temp = data.pop(0)
            if temp!=None:
                root.left = TreeNode(temp)
                r.append(root.left)
            temp = data.pop(0)
            if temp!=None:
                root.right = TreeNode(temp)
                r.append(root.right)
            self.buildTreeByList(r,data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
