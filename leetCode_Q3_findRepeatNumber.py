'''
面试题03. 数组中重复的数字
找出数组中重复的数字。
在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

题解：
这道题在原书上绝对不是简单级别啊！
它考察的是程序员的沟通能力，先问面试官要时间/空间需求！！！
只是时间优先就用字典，
还有空间要求，就用指针+原地排序数组，
如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！
'''

# test :
# input: [] -> None
# 1. [1, 2, 3, 4] -> None
# 2. [1, 2, 4, 0, 1] -> 1
# 3. [1, 2, 3, 4, ..., 90, 91, 92, 92]->92

# 执行用时 :64 ms, 在所有 Python3 提交中击败了48.24%的用户
# 内存消耗 :23 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums==[]:
            return 
        ans = set()
        for num in nums:
            if num in ans:
                return num
            else:
                ans.add(num)
        return

'''
# 执行用时 :48 ms, 在所有 Python3 提交中击败了90.09%的用户
# 内存消耗 :23.2 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums==[]:
            return 
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                return nums[i]
'''

'''
# 执行用时 :64 ms, 在所有 Python3 提交中击败了48.24%的用户
# 内存消耗 :23.1 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        if nums==[]:
            return 
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
        return 
'''
