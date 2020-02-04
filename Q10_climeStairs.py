# Fabonacci
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            a = 1 
            b = 2
            for i in range(3,n):
                temp = a
                a = b 
                b = b + temp
            return a+b
