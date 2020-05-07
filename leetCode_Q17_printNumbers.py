'''
面试题17. 打印从1到最大的n位数
输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
 
说明：
用返回一个整数列表来代替打印
n 为正整数
'''

# 执行用时 :56 ms, 在所有 Python3 提交中击败了44.42%的用户
# 内存消耗 :19.4 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        if n<=0:
            return
        init = '9'*n
        maxN = int(init)
        ans = list(range(1,maxN+1))
        return ans

