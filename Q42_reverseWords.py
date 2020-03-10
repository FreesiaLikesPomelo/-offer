'''
面试题58 - I. 翻转单词顺序
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
示例 1：
输入: "the sky is blue"
输出: "blue is sky the"
示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：
输入: "a good   example"
输出: "example good a"
解释: 如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
说明：
无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
'''

# test cases:
# 1. s = '', return ''
# 2. s only contain one word: return s; s only contains space " "
# 3. function test

# 执行用时 :44 ms, 在所有 Python3 提交中击败了50.42%的用户
# 内存消耗 :13.8 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def reverseWords(self, s: str) -> str:
        if s=='':
            return s
        
        temp = s.split() # list of the words
        if len(temp)==0:
            return ''
        
        res = ''
        for i in temp:
            if res!='':
                t = i + ' ' + res
            else:
                t = i
            res = t
        return res

'''
#执行用时 :56 ms, 在所有 Python3 提交中击败了23.95%的用户
#内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def reverseWords(self, s: str) -> str:
        if s=='':
            return ''
        
        idx1 = 0
        idx2 = 0
        res = ''
        end = len(s)-1
        if s[0]!=' ': 
            # the first char in s is not space, 
            # find the first space, and then copy the first word to res.
            while s[idx1]!=' ':
                if idx1==end:
                    return s # s only contain one word
                idx1+=1
            # copy the first word
            res+=s[0:idx1]
            # now idx1 points the first space

        while idx1<=end and idx2<=end:
            while s[idx1]==' ':
                if idx1==end:
                    return res # s only contains space ' ', no other character 
                idx1+=1 # find first character
            idx1-=1 # idx1 pointing the last space, 
            idx2 = idx1+1
            while s[idx2]!=' ':
                if idx2==end:
                    # s[idx1+1:] is the last word
                    if res!='':
                        temp = s[idx1+1:]+' '+res
                    else:
                        temp = s[idx1+1:]
                    res = temp
                    return res
                idx2+=1
            # idx2 pointing the first space,
            if res!='':
                temp = s[idx1+1:idx2]+' '+res
            else:
                temp = s[idx1+1:idx2]
            res = temp # update res
            idx1 = idx2 # start a new round
        
        return res
'''

        
