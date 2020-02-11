# -*- coding:utf-8 -*-
'''
Analysis
N = 1  f(1)=I~1
N = 2  f(2)=I~1+—~1
N = 3  f(3)=I~f(2) + —~f(1) 
N = 4  f(4)= I~f(3)+ —~f(2)
N = n  f(n) = I~f(n-1)+—~f(n-2)
'''
class Solution:
    def rectCover(self, number):
        # write code here
        former = 1
        latter = 1
        if number<1:
            return 0
        elif number==1:
            return latter
        else: # recursive solution
            for i in range(1,number):
                s = former+latter
                former = latter
                latter = s
            return s
