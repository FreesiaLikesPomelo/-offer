# F(0)=0 F(1)=1 F(2)=1 F(3)=2
# 执行用时：44 ms, 在所有 Python3 提交中击败了42.84%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def fibS(self,fa:int,fb:int,id:int,n:int)-> int:
        if id==n:
            fn = fa+fb
            return fn%1000000007
        else:
            return self.fibS(fb,fa+fb,id+1,n)

    def fib(self, n: int) -> int:
        if n<0:
            return None
        if n==0:
            return 0
        if n==1:
            return 1
        fa = 0
        fb = 1
        return self.fibS(fa,fb,2,n)

'''
# 执行用时：40 ms, 在所有 Python3 提交中击败了68.37%的用户
# 内存消耗：13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def fib(self, n: int) -> int:
        if n<0:
            return None
        if n==0:
            return 0
        if n==1:
            return 1
        fa = 0
        fb = 1
        for i in range(1,n):
            fn = fa+fb
            if n-1==i:
                return fn%1000000007
            else:
                fa = fb
                fb = fn
'''
