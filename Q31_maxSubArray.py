# all negative numbers
#

'''
输入一个整型数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。

执行用时 :68 ms, 在所有 Python3 提交中击败了95.41%的用户
内存消耗 :17.2 MB, 在所有 Python3 提交中击败了100.00%的用户
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if nums==[]:
            return None
        result = 0
        temp = 0
        negCount = 0
        for i in range(len(nums)):
            if nums[i]<0: 
                negCount+=1
                if result<=0: # ignore negative numbers at first
                    continue
                else: # reult > 0 
                    if nums[i]+temp<0: # maintain former temp
                        temp = 0
                    else:
                        temp = nums[i]+temp
            else:
                if result==temp:
                    result+=nums[i]
                    temp = result
                else:
                    temp = temp+nums[i]
                    if temp>result:
                        result = temp
                    else:
                        continue  
            #print("i:",i,"result:",result,"temp:",temp)
        if negCount==len(nums):# all negative numbers
            return max(nums)
        else:
            return result

