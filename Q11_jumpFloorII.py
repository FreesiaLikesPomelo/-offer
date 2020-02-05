# -*- coding:utf-8 -*-
'''
f(0)=1
1:f(1)=1~f(0)=1
2:f(2)=1~f(1)+2~f(0)=2
3:1~f(2)+2~f(1)+3~f(0) = 2 + 1 + 1
4:1~f(3)+2~f(2)+3~f(1)+4~f(0)
n:1~f(n-1)+2~f(n-2)+3~f(n-3)+……+(n-1)~f(1)+n~f(0)
f(n)=f(n-1)+f(n-2)+...+f(1)+f(0)
'''
class Solution:
    def listSum(self,fn):
        s = 0
        for i in range(len(fn)):
            s = fn[i]+s
        return s
    
    def jumpFloorII(self,number):
        # write code here
        fn=[]
        fn.append(1)
        fn.append(1)
        fn.append(1+1)
        if number > 2:
            for i in range(2,number):
                fn.append(self.listSum(fn))
        return fn[number]
