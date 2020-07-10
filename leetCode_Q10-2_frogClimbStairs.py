class Solution:
    # 执行用时：48 ms, 在所有 Python3 提交中击败了19.01%的用户
    # 内存消耗：13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
    def frogRec(self,n:int,id:int,fa:int, fb:int)->int:# n starts from 3
        if n==id:
            fn = fa+fb
            return fn
        else:
            fn = self.frogRec(n,id+1,fb,fb+fa)
            return fn
    # 执行用时：56 ms, 在所有 Python3 提交中击败了5.82%的用户
    # 内存消耗：13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
    
    def frog(self, n: int)->int:
        fa = 1
        fb = 2
        for i in range(2,n): # n starts from 3
            fn = fa+fb
            if n==i+1:
                return fn%1000000007
            else:
                fa = fb
                fb = fn

    def numWays(self, n: int) -> int:
        if n<=0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2

        #fn = self.frog(n-1)+self.frog(n-2)
        #return self.frog(n)
        fn = self.frogRec(n,3,1,2)
        return fn%1000000007
