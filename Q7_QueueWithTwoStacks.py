# -*- coding:utf-8 -*-
# we can use one stack to store the
''' 
test case
1.往空队列里面添加、删除
2.往非空队列添加、删除
3.连续删除元素直至队列为空
'''
class Solution:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        # write code here
        self.stack1.append(node)
        
    def pop(self):
        # return xx
        if len(self.stack2)>0: # if there is numbers in stack2, pop it first.
            return self.stack2.pop()
        else: 
        # if stack2 is empty, pop all the number from stack1 to stack2, then pop it
            if len(self.stack1)>0:
                while self.stack1:
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
            else:
                return None
