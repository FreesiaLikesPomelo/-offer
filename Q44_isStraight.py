'''
面试题61. 扑克牌中的顺子
难度简单
从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。审题认真点儿啊。。
示例 1:
输入: [1,2,3,4,5]
输出: True
示例 2:
输入: [0,0,1,2,5]
输出: True
限制：
数组长度为 5 
数组的数取值为 [0, 13] .
来自 <https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/> 

执行用时 :40 ms, 在所有 Python3 提交中击败了49.06%的用户
内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. 10,J,Q,K,A √
# 2. J,Q,K,A,1 ×
# 3. normal True ： list.sort() 遍历一遍得出+=1，√
# 4. count 0, [0,0,2,3,5] √ [0,0,2,3,6]√ [0,0,2,3,7]×

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if len(nums)<5:
            return False
        
        nums.sort()
        count0 = 0
        idx = 0
        while nums[idx]==0:
            count0+=1
            idx+=1
        # now idx pointing the first non-0 number
        # count0 denotes the numbers of 0
        start = nums[idx]
        # if nums contains 1
        
        idx+=1
        while idx<len(nums):
            #print("nums:",nums,"start",start,"nums[",idx,"]=",nums[idx])
            if nums[idx]==start:
                #print("there are two same numbers in nums:", nums)
                return False
            elif nums[idx]-start==1:
                start = nums[idx]
                if idx==len(nums)-1:
                    return True
                idx+=1
            else: 
                if count0>0:
                    start+=1
                    count0-=1
                else:
                    break
        if idx<len(nums)-1:
            # count==0, but still didn't reach the last number in nums
            #print("now the idx is",idx,"nums[idx]=",nums[idx],"count0",count0)
            return False 
        else:
            if nums[idx]-start>1:
                #print("now the idx is",idx,"nums[idx]=",nums[idx],"start",start)
                return False
            return True
        

# s = Solution()
# a = [10,0,0,0,1]
# print(s.isStraight(a))
