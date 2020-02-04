'''
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N ==1:
            return 1
        else:
            while N>1:
                return self.fib(N-1)+self.fib(N-2)
'''
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        elif N ==1:
            return 1
        else:
            a = 0
            b = 1
            for i in range(2,N):
                temp = a
                a = b
                b = temp+b
            return a+b

