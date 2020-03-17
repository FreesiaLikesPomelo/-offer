'''
面试题63. 股票的最大利润
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
限制：
0 <= 数组长度 <= 10^5
'''

# test cases:
# 1. array = []
# 2. array is [7,6,4,3,1], return 0
# 3. array is [7,3,6,4,1], return 6-3
# 4. array is [7,3,3,3,3], return 0
# 5. array is [6,7,2,2,5], return 5-2
# 6. array is [3,2,6,5,0,3]

# 执行用时 :44 ms, 在所有 Python3 提交中击败了83.42%的用户
# 内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        plen = len(prices)
        if plen==0 or plen==1:
            return 0

        minPrice = sys.maxsize
        maxPro = 0
        for i in range(plen):
            minPrice = min(minPrice,prices[i])
            maxPro = max(prices[i]-minPrice,maxPro)
            # print(minPrice,maxPro)
        return maxPro

'''
# 6456 ms	14.4 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]:
            return 0
        if len(prices)==1:
            return 0
        maxPro = 0
        plen = len(prices)
        for i in range(plen-1):
            maximum = max(prices[i+1:])
            tempProfit = maximum - prices[i]
            #print("prices[",i,"]:",prices[i],"maximum:",maximum,"maxPro",maxPro,"tempProfit:",tempProfit)
            if tempProfit>maxPro:
                maxPro = tempProfit
        return maxPro
'''
