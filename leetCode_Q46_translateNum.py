'''
面试题46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
提示：
0 <= num < 231
'''

# test cases:
# 1. num <0:  return 0
# 2. 0=<num<=9: rturn 1
# 3. 623->2, 506->1, 220->3,12258->5, 10001-> 2

# 执行用时 :32 ms, 在所有 Python3 提交中击败了89.41%的用户
# 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def transNums(self,nums: str,current_count:int)->int:
        numLen = len(nums)
        # print("transNum",nums,numLen,current_count)
        if numLen==0:
            return 0
        elif numLen==1:
            return 1
        elif numLen==2:
            if int(nums)<=9:
                return 1
            elif int(nums)<=25:
                return 2
            else:
                return 1
        else:
            first = self.transNums(nums[1:],current_count)
            if int(nums[0:2])>25 or  int(nums[0:2])<10:
                second = 0
                # print(nums[0:2])
            else:
                second = self.transNums(nums[2:],current_count)
            # print(nums,current_count,first,second)
            return first + second + current_count

    def translateNum(self, num: int) -> int:
        if num<0:
            return 0
        elif num>=0 and num<=9:
            return 1
        elif num>=10 and num<=25:
            return 2
        else:
            nums = str(num)
            ans = self.transNums(nums,0)
            return ans
