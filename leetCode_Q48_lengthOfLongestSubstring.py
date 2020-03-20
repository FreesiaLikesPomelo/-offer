'''
面试题48. 最长不含重复字符的子字符串
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
 提示：
s.length <= 40000
'''

# --- 2 methods --- #
# --- dynamic programing --- #
# --- sliding window --- #

# test cases:
# 1. empty string: return 0
# 2. function test

# --- dynamic programing --- #
# 执行用时 :64 ms, 在所有 Python3 提交中击败了91.11%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0
        dic = {}
        curLength = 0
        maxLength = 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
                curLength+=1
            else:
                d = i - dic.get(s[i])
                dic[s[i]]=i
                if d<=curLength:
                    curLength = d
                else:
                    curLength +=1
            maxLength = max(curLength,maxLength)
        return maxLength


'''
# --- sliding window 1 --- #
# 执行用时 :72 ms, 在所有 Python3 提交中击败了79.56%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0

        low = 0
        count = 1
        res = 1
        dic = {s[0]:0}
        for i in range(1,len(s)):
            if s[i] not in s[low:i]: # not in the former string
                count+=1
                res = max(count,res)
                dic[s[i]] = i
                # print(s[low:i+1])
            else:
                low = dic.get(s[i])+1
                dic[s[i]] = i
                count = i-low+1
                res = max(count,res)
                # print("in:",s[low:i+1])
        return res
# --- sliding window 2 --- #
# 执行用时 :88 ms, 在所有 Python3 提交中击败了49.77%的用户
# 内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=='':
            return 0

        low = 0
        count = 1
        res = 1
        for i in range(1,len(s)):
            if s[i] not in s[low:i]: # not in the former string
                count+=1
                res = max(count,res)
                # print(s[low:i+1])
            else:
                while s[i] in s[low:i]:
                    low+=1
                    count = i-low+1
                    res = max(count,res)
                    # print("in:",s[low:i+1])
        return res
'''                
            
