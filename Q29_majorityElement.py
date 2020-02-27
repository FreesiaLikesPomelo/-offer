'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
来自 <https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/> 

示例 1:
输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
输出: 2

执行用时 :60 ms, 在所有 Python3 提交中击败了83.37%的用户
内存消耗 :15 MB, 在所有 Python3 提交中击败了100.00%的用户
'''


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums==[]:
            return None
        if len(nums)==1:
            return nums[0]
        
        result = nums[0]
        times = 1
        for i in range(1,len(nums)):
            if nums[i]==result:
                times+=1
            else:
                times-=1
                if times==0:
                    result = nums[i]
                    times+=1
        return result
