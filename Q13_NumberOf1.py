# -*- coding:utf-8 -*-
'''
positive number： 9:0000 1001
negative number：-9:invert（0000 1001 - 1）=1111 0111
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        flag = 1
        count = 0
        for i in range(32):
            if(n&flag):
                count+=1
            flag = flag<<1
        return count
#s=Solution()
#print(s.NumberOf1(-9))
