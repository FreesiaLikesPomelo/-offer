'''
面试题60. n个骰子的点数
难度简单
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
 你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
 示例 1:
输入: 1
输出: [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
示例 2:
输入: 2
输出: [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]
限制：
1 <= n <= 11
来自 <https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/> 
'''

# test cases:
# 1. n<=0: return []
# 2. function test

#执行用时 :52 ms, 在所有 Python3 提交中击败了28.30%的用户
#内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def twoSum(self, n: int)->List[float]:
        if n<=0:
            return []

        unit = pow((1/6),n)
        if n==1:
            res = [unit]*6
            return res
        
        sCount = [[],[]] 
        sCount[0] = [1]*6+[0]*6*(n-1) # first dice
        sCount[1] = [0]*6*n
        flag = 0
        #print("第",1,"个骰子的结果是：",sCount[flag])
        for diceNo in range(2,n+1):
            # for rest dices 
            # print("第",diceNo,"个骰子的结果是：",sCount[flag])
            flag = (diceNo-1)%2 # when diceNo is even Number,flag should be 1
            for sn in range(diceNo,diceNo*6+1): # update the value in sCount[flag][diceNo-1,diceNo*n]
                # for the sum of diceNo dices
                # print(diceNo,"个骰子和为",sn,"的出现次数求解。")
                for i in range(1,7): # i in [1,6]
                    if i==1:
                        sCount[flag][sn-1]=0 # set the value as 0
                    if sn-i>=diceNo-1:
                        sCount[flag][sn-1]+=sCount[diceNo%2][sn-1-i]
                        # when diceNo is 2,flag should be 1
                        #print("上一个数组中和为",sn-i,"坐标为：",sn-1-i,"的出现次数为：",sCount[flag%1][sn-1-i],"diceNo%2",diceNo%2)
                #print(diceNo,"个骰子和为",sn,"的出现次数为：",sCount[flag][sn-1])
            #print("第",diceNo,"个骰子的结果是：",sCount[flag])
        res = sCount[flag][diceNo-1:]
        for i in range(len(res)):
            res[i] = res[i]*unit
        return res
                

'''
# recursion algorithm: cost too much time, can only work when n in [1,8]
class Solution:
    def probability(self, sCount:List[int], n:int):
        for i in range(1,7):
            self.sumCount(sCount, n, n, i)

    def sumCount(self, sCount:List[int], n:int, curdice:int, sn: int):
        # curdice: the No.of dices, start from to n->1
        # sn: the sum of rest dices
        # n: the number of dices
        # return the sum of the 
        # calculate how many times each sum appeared of n dices
        if curdice==1:
            sCount[sn-n]+=1
        else:
            for i in range(1,7):
                self.sumCount(sCount, n, curdice-1, sn+i)

        
    def twoSum(self, n: int) -> List[float]:
        if n<=0:
            return []
        
        smallest = n
        biggest = 6*n
        sCount = [0]*(biggest-smallest+1) # how many times the s has appeared.
        self.probability(sCount,n)
        print("sCount:",sCount)

        res = []
        unit = pow((1/6),n)
        for i in range(len(sCount)):
            res.append(sCount[i]*unit)
        return res
'''
#s = Solution()
#n = 10
#print(s.twoSum(n))
