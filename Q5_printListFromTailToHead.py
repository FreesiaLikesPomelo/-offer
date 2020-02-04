# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
# solution 1
from collections import deque
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if(listNode==None):
            return []
        else:
            #q = LifoQueue()
            q = deque()
            while listNode:
                q.appendleft(listNode.val)
                listNode = listNode.next
            return q
'''

''' 
# solution 2
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if(listNode==None):
            return []
        else:
            l=[]
            while listNode:
                l.append(listNode.val)
                listNode=listNode.next
            return l[::-1]
'''

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if(listNode==None):
            return []
        else:
            l=[]
            while listNode:
                l.append(listNode.val)
                listNode=listNode.next
            l.reverse()
            return l
