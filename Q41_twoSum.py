'''
面试题57. 和为s的两个数字
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
限制：
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6

执行用时 :188 ms, 在所有 Python3 提交中击败了61.37%的用户
内存消耗 :25.4 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. nums=[],return[]
# 2. function test: cannot find two qualified numbers,normal test
# 3. are all the numbers in nums positive?

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if nums==[]:
            return []

        if nums[0]>target:
            return []
        #elif nums[-1]<target and nums[-1]+nums[-2]<target:
        #    return []
        else:
            ahead = 0
            behind = len(nums)-1
            temp = nums[ahead]+nums[behind]
            while temp!=target and ahead<behind:
                if temp>target:
                    behind-=1
                else:# temp<target
                    ahead+=1
                temp = nums[ahead]+nums[behind]
            if temp==target:
                return [nums[ahead],nums[behind]]
            else:
                return []
                