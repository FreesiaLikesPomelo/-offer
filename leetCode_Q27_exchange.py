'''
面试题21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4] 
注：[3,1,2,4] 也是正确的答案之一。
提示：
1 <= nums.length <= 50000
1 <= nums[i] <= 10000
'''
# test cases:
# [2]: return [2]
# [1,2,3,4]: return [1,3,2,4]
# [1,1,1,1]: return [1,1,1,1]
# [2,2,2,2]: return [2,2,2,2]
# [0,1,2,3]: return [3,1,2,0]

# 执行用时 :60 ms, 在所有 Python3 提交中击败了67.78%的用户
# 内存消耗 :17.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        nlen = len(nums)
        if nlen<=1:
            return nums
        odd = []
        even = []
        for i in range(nlen):
            if nums[i]%2==1:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        return odd+even
'''
# 执行用时 :120 ms, 在所有 Python3 提交中击败了19.95%的用户
# 内存消耗 :18 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        print(nums)
        nlen = len(nums)
        if nlen<=1:
            return nums
        peven = 0
        podd = nlen - 1
        while podd-peven>1:
            if int(nums[peven]%2)==1: # first num is odd shift point backward
                peven+=1 
            if int(nums[podd]%2)==0: # first num is even shift point forward
                podd-=1
            if int(nums[peven]%2)==0 and int(nums[podd]%2)==1:
                #print("switch",peven,podd)
                temp = nums[peven]
                nums[peven] = nums[podd]
                nums[podd] = temp
                #print(nums)
        return nums
'''
            
