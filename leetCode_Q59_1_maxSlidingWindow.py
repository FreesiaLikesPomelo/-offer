'''
面试题59 - I. 滑动窗口的最大值
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
提示：
你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。

执行用时 :128 ms, 在所有 Python3 提交中击败了59.06%的用户
内存消耗 :17 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

class Solution:
    def getMaxNum(self,nums:List[int]):
        # return maxNum and maxIdx
        maxNum = 0 
        maxIdx = 0
        for i in range(len(nums)):
            if maxNum<=nums[i]:
                maxNum = nums[i]
                maxIdx = i
        return maxNum,maxIdx

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if nums==[]:
            return []
        if k==1:
            return nums
        if k==len(nums):
            return [max(nums)]

        maxNum, maxIdx = self.getMaxNum(nums[:k])
        res = []
        res.append(maxNum)       
        for i in range(k,len(nums)):
            if nums[i]>maxNum:
                maxNum = nums[i]
                res.append(maxNum)
                maxIdx = i
            else:
                # nums[i]<maxNum, but now maxNum is not in nums[k-2,k]
                if i-(k-1)<=maxIdx:
                    res.append(maxNum)
                else:
                    if i==len(nums)-1:
                        maxNum,maxIdx = self.getMaxNum(nums[i-(k-1):])
                    else:
                        maxNum,maxIdx = self.getMaxNum(nums[i-(k-1):i+1])
                    res.append(maxNum)
        return res


            
