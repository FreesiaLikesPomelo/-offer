# test cases:
# 1. empty string
# 2. only have one caracter
# 3. more than one without same element in it
# 4. with same element

'''
输入一个字符串，打印出该字符串中字符的所有排列。
你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
示例:
输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

执行用时 :472 ms, 在所有 Python3 提交中击败了23.71%的用户
内存消耗 :17.8 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

class Solution:
    def swapStr(self, s:str, i:int, j:int)->str:
        if i==j:
            return s
        # replace the ith element and jth element in s
        temp = ''
        for idx in range(len(s)):
            if idx==i:
                temp=temp+s[j]
            elif idx==j:
                temp=temp+s[i]
            else:
                temp = temp+s[idx]
        return temp

    def permutation(self, s: str) -> List[str]:
        if s=='':
            return []

        if len(s)==1:
            return [s]
        
        result = []
        # split str into two parts
        for i in range(len(s)):
            if i!=0 and s[i]==s[0]: # if there are two same elements
                #print("s[",i,"]==s[",0,"]","s[i]=",s[i],"s[0]",s[0])
                continue
            else:
                first = s[i] # choose the first element one by one
                tempS = self.swapStr(s,0,i)
                temp = self.permutation(tempS[1:])
                for i in range(len(temp)):
                    tempResult = first + temp[i]
                    result.append(tempResult)
                #print("i:",i,"first:",first,"tempS[1:]:",tempS[1:],"temp:",temp,"tempResult:",tempResult,"result",result)
        result=list(set(result))
        return result


