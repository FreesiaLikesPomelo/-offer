'''
面试题64. 求1+2+…+n
难度中等
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
 示例 1：
输入: n = 3
输出: 6
示例 2：
输入: n = 9
输出: 45
限制：
	• 1 <= n <= 10000

来自 <https://leetcode-cn.com/problems/qiu-12n-lcof/> 

执行用时 :52 ms, 在所有 Python3 提交中击败了46.01%的用户
内存消耗 :21.3 MB, 在所有 Python3 提交中击败了100.00%的用户
'''
class Solution:
    def __init__(self):
        self.S = 0

    def addS(self, n:int)-> bool:
        self.S+=n
        n-=1
        return n>0 and self.addS(n)

    def sumNums(self, n: int) -> int:
        self.addS(n)
        return self.S
