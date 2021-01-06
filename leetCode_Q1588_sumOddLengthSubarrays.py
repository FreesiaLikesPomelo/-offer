"""
1588. 所有奇数长度子数组的和
给你一个正整数数组 arr ，请你计算所有可能的奇数长度子数组的和。
子数组 定义为原数组中的一个连续子序列。
请你返回 arr 中 所有奇数长度子数组的和 。

示例 1：
输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
示例 2：
输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
示例 3：
输入：arr = [10,11,12]
输出：66

提示：
1 <= arr.length <= 100
1 <= arr[i] <= 1000

执行用时：64 ms, 在所有 Python3 提交中击败了59.46%的用户
内存消耗：14.7 MB, 在所有 Python3 提交中击败了13.15%的用户
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr)==0:
            return 0
        elif len(arr)==1:
            return arr[0]
        elif len(arr)==2:
            return arr[0]+arr[1]
        else:
            n = int(len(arr)/2)
            result = 0
            for i in range(n):
                start = 0
                end = 1+2*i
                while end<=len(arr):
                    #print(arr[start:end])
                    result+=sum(arr[start:end])
                    start+=1
                    end = start+1+2*i
            if len(arr)%2!=0:
                result+=sum(arr)
                return result
            else:
                return result
