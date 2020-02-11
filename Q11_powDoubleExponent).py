# -*- coding:utf-8 -*-
import math

class Solution:
    def _pow(self,base,exponent):
        solution = base
        if exponent==0:
            return 1
        for i in range(abs(exponent)-1):
            solution=solution*base
        if exponent<0:
            solution = 1/solution
        return solution
    
    def Power(self, base, exponent):
        # write code here
        if base==0.0:
            if exponent<0:
                inputInvilid=1
                solution = 0.0
            elif exponent==0: #0^0 is meaning less.
                solution = 1.0
            else:
                solution = 0.0
        else:
            solution = math.pow(base,exponent)
            #solution = self._pow(base,exponent)
        return solution
