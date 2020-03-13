'''
面试题67. 把字符串转换成整数
难度中等
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
在任何情况下，若函数不能进行有效的转换时，请返回 0。
说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
示例 1:
输入: "42"
输出: 42
示例 2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
     因此返回 INT_MIN (−231) 。
注意：本题与主站 8 题相同：https://leetcode-cn.com/problems/string-to-integer-atoi/
来自 <https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/> 

执行用时 :68 ms, 在所有 Python3 提交中击败了9.54%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. input: '   ','xxe',''->return 0 假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换
# 2. input: '   +798xx'->798; '   -193 x'->-193
#    how about input " ++120 x"-> should I return 120? or 0?
# 3. long: if not in [−2**31,  2**31 − 1];  return INT_MAX (231 − 1) 或 INT_MIN (−231) 

flag = 0 # -1, empty str; -2,第一个非空格字符不是一个有效整数字符; -3,仅包含空白字符; 
small = -pow(2,31)
big = -small-1

class Solution:
    def strToInt(self, str: str) -> int:
        global flag
        global small
        global big
        if str=='':
            flag = -1
            #print("empty string! flag = ", flag)
            return 0
        
        if str.isdigit(): # only positive intergers can pass this one.
            #print("only positive numbers")
            res = int(str)
            if res>big:
                return big
            else:
                return res

        # test if the first non-space character is a number or '+','-'
        idx = 0
        slen = len(str)
        while idx<slen and str[idx]==' ':
            idx+=1

        if idx==slen:
            flag = -3
            #print("only containing spaces! flag = ", flag)
            return 0
        
        # check if it's '+','-',or number
        isPositive = 1 
        numFlag = str[idx].isdigit() # is it a number;
        if not numFlag:
            if idx==slen-1: # now it's the last letter '  +/-/x'
                return 0
            elif str[idx]=='+':
                isPositive = 1
                idx+=1
            elif str[idx]=='-':
                isPositive = 0
                idx+=1
            else:
                flag = -2
                #print("the first letter is not a number or '+','-'! flag = ", flag)
                return 0

        # check now if str[idx] is a number or not: if not, return 0
        if not str[idx].isdigit():
            # if str[idx]=='+' or '-', do we need to check next?
            return 0
        # find the first non-number letter in string
        else:
            start = idx # store the first number index
            while idx<slen and str[idx].isdigit():
                idx+=1
            # while end: meet first non-number letter / idx==len
            if idx==len:
                res = int(str[start:])
            else:
                res = int(str[start:idx])
            # denoting it's positive or negtive
            # make sure if it's in the requested range [−2**31,  2**31 − 1]
            if isPositive==0: # negative
                res = -res
                if res<small:
                    return small
                else:
                    return res
            else:
                if res>big:
                    return big
                else:
                    return res

#s = Solution()
#print(s.strToInt("   -42"))
#print(s.strToInt("4193 with words"))
#print(s.strToInt("words and 987"))
#print(s.strToInt("-91283472332"))


