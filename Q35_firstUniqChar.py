'''
面试题50. 第一个只出现一次的字符
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。
示例:
s = "abaccdeff"
返回 "b"
s = "" 
返回 " "
限制：
0 <= s 的长度 <= 50000

执行用时 :132 ms, 在所有 Python3 提交中击败了55.68%的用户
内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. s='' return ' '
# 2. function test

class Solution:
    def firstUniqChar(self, s: str) -> str:
        if s=='':
            return ' '
        
        slist = list(s)
        dic = {}
        for i in slist:
            if not i in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        
        for i in slist:
            if dic[i]==1:
                return i
        return ' '
