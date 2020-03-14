'''
面试题66. 构建乘积数组
难度简单
给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
示例:
输入: [1,2,3,4,5]
输出: [120,60,40,30,24]
提示：
	• 所有元素乘积之和不会溢出 32 位整数
	• a.length <= 100000
来自 <https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/> 

执行用时 :96 ms, 在所有 Python3 提交中击败了58.76%的用户
内存消耗 :23.3 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# B[i] = A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]
# B[i] = C[i]*D[n-1-i]
# C[i] = 1*A[0]*A[1]*...*A[i-1] -> C[0]=1
# D[n-1-i] = A[n-1]*A[n-2]*...*A[i+1]*1 ->D[n-1]=1

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        if a==[]:
            return []
        if len(a)==1:
            return a
        
        c = []
        c.append(1) # c[0]=1
        d = []
        d.append(1)
        n = len(a)
        for i in range(n-1):
            c.append(c[-1]*a[i])
            d.append(d[-1]*a[n-1-i])
        # print("c:",c)
        # print("d:",d)
        b = []
        for i in range(n):
            b.append(c[i]*d[n-1-i])
        # print("b:",b)
        return b
