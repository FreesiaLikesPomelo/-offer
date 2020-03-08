'''
面试题51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
限制：
0 <= 数组长度 <= 50000
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/

执行用时 :1564 ms, 在所有 Python3 提交中击败了85.67%的用户
内存消耗 :18.5 MB, 在所有 Python3 提交中击败了100.00%的用户
'''


# merge-sort
# test cases:
# 1. input [] or [int]:return 0
# 2. function test: input sorted array: return

class Solution:
    def merge(self, left: List[int], right: List[int]):
        # return sortedList:List[int],inverNum:int
        lidx = len(left)-1
        ridx = len(right)-1
        idx = ridx+lidx+1
        result = list(range(idx+1))
        inverNum = 0

        while lidx>=0 and ridx>=0:
            if left[lidx]>right[ridx]:
                inverNum+=(ridx+1)
                result[idx] = left[lidx]
                idx-=1
                lidx-=1
            else:
                result[idx] = right[ridx]
                idx-=1
                ridx-=1
        
        if lidx<0:
            # right list was left
            while ridx>=0:
                result[idx] = right[ridx]
                idx-=1
                ridx-=1
        if ridx<0:
            while lidx>=0:
                result[idx] = left[lidx]
                idx-=1
                lidx-=1

        return result, inverNum

    def mergeSort(self, nums: List[int]):
        # return sortedList:List[int],inverNum:int
        if len(nums)<=1:
            return nums, 0
        mid = int(len(nums)/2)
        inverNum = 0
        left,lInverNum = self.mergeSort(nums[:mid])
        right,rInverNum = self.mergeSort(nums[mid:])
        result,tempInv = self.merge(left,right)
        tempInv = lInverNum+rInverNum+tempInv
        return result, tempInv

    def reversePairs(self, nums: List[int]) -> int:
        if nums==[] or len(nums)==1:
            return 0
        
        resList, inverNum = self.mergeSort(nums)
        return inverNum
