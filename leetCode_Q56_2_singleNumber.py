'''
面试题56 - II. 数组中数字出现的次数 II
在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
示例 1：
输入：nums = [3,4,3,3]
输出：4
示例 2：
输入：nums = [9,1,7,9,7,9,7]
输出：1
限制：
1 <= nums.length <= 10000
1 <= nums[i] < 2^31
'''

# test cases:
# 1. len(nums) < 4: return nums
# 2. function test

# 执行用时 :56 ms, 在所有 Python3 提交中击败了89.99%的用户
# 内存消耗 :14.5 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def storeToHMap(self, nums: List[int],hmap: dict):
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]]+=1
                # print("hmap[",nums[i],"]=",hmap[nums[i]])
            else:
                hmap[nums[i]]=1

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)<4:
            return nums
        hmap={}
        self.storeToHMap(nums,hmap)
        for i,j in hmap.items():
            if j==1:
                return i

'''      
# 执行用时 :60 ms, 在所有 Python3 提交中击败了86.15%的用户
# 内存消耗 :14.8 MB, 在所有 Python3 提交中击败了100.00%的用户  
class Solution:
    def storeToHMap(self, nums: List[int],hmap: dict):
        for i in range(len(nums)):
            if nums[i] in hmap:
                hmap[nums[i]]+=1
                # print("hmap[",nums[i],"]=",hmap[nums[i]])
                if hmap[nums[i]]==3:
                    del hmap[nums[i]]
            else:
                hmap[nums[i]]=1

    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)<4:
            return nums
        hmap={}
        self.storeToHMap(nums,hmap)
        res = list(hmap.keys())
        return res[0]
'''
