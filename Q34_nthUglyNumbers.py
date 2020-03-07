'''
面试题49. 丑数
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
示例:
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  
1 是丑数。
n 不超过1690。

执行用时 :132 ms, 在所有 Python3 提交中击败了98.45%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# using space to decrease needed time 
# test cases:
# if n<=0: return None:
# unList = [1,2,3,4,5] 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n<=0:
            return None
        
        unList = [1,2,3,4,5]
        if n<=5:
            return unList[n-1]
        # n>5
    
        m2 = 1
        m3 = 1
        m5 = 1
        idx2 = 2
        idx3 = 1
        idx5 = 1
        while len(unList)<n:
            maxUN = unList[-1]
            while m2<=maxUN:
                m2 = unList[idx2]*2
                idx2+=1
            while m3<=maxUN:
                m3 = unList[idx3]*3
                idx3+=1
            while m5<=maxUN:
                m5 = unList[idx5]*5
                idx5+=1
            if m2<=m3:
                if m2<=m5:
                    unList.append(m2)  
                else: # m2>m5
                    unList.append(m5)  
            else: # m2>m3
                if m3<=m5:
                    unList.append(m3)
                else:
                    unList.append(m5)
        return unList[-1]
