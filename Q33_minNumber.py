'''
面试题45. 把数组排成最小的数
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
示例 1:
输入: [10,2]
输出: "102"
示例 2:
输入: [3,30,34,5,9]
输出: "3033459"

执行用时 :56 ms, 在所有 Python3 提交中击败了62.90%的用户
内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

import functools

def cmp(a: int, b: int)->int:
    temp = int(str(a)+str(b))-int(str(b)+str(a))
    if temp==0:
        return 0
    elif temp>0:
        return 1
    else: 
        return -1

class Solution:
    def minNumber(self, nums: List[int]) -> str:
        if not nums:
            return ''
        
        array = sorted(nums, key=functools.cmp_to_key(cmp))
        # design new rule:
        # for two numbers: n, m 
        # if nm>mn: n>m
        print(array)
        ans = ''
        #return ''.join([str(i) for i in array])
        for i in array:
            ans = ans+str(i)
        return ans
