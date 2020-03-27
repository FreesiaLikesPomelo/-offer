'''
面试题43. 1～n整数中1出现的次数
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
示例 1：
输入：n = 12
输出：5
示例 2：
输入：n = 13
输出：6
限制：
1 <= n < 2^31

执行用时 :40 ms, 在所有 Python3 提交中击败了55.05%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1<=n<=9: return 1
# n = 10: return 2
# n = 20: return 12

class Solution:
    def countOne(self, n:int)->int:
        if n==0:
            return 0
        if n<=9:
            return 1
        
        strN = str(n)
        digit = len(strN)
        high = int(strN[0])
        highPow = pow(10,digit-1)
        last = int(strN[1:])
        # print("n:",n, "high:",high, "highPow:",highPow,"last:",last)

        if high==1:
            # 1234
            # 1~999
            temp1 = self.countOne(highPow-1)
            # 1000~1234 & 1 in highest digit
            temp2 = last+1
            temp3 = self.countOne(last)
            return temp1+temp2+temp3
        else:
            # 3290
            # 1~999  2000~2999 & 1000~1999
            temp1 = high*self.countOne(highPow-1)
            # 1000~1999
            temp2 = highPow
            # 3000~3290
            temp3 = self.countOne(last)
            return temp1+temp2+temp3        

    def countDigitOne(self, n: int) -> int:
        if n<1:
            return 0
        return self.countOne(n)
