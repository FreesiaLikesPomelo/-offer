'''
面试题53 - II. 0～n-1中缺失的数字
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
示例 1:
输入: [0,1,3]
输出: 2
示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
限制：
1 <= 数组长度 <= 10000
'''

# 执行用时 :36 ms, 在所有 Python3 提交中击败了95.95%的用户
# 内存消耗 :14.2 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nlen = len(nums)
        if nlen==0:
            return None
        if nums[0]!=0:
            return 0
        if nums[nlen-1]==nlen-1:
            return nlen # cause it
        if nlen==2: #[0,1],[1,2],[0,2]
            return 1
        start = 0
        end = nlen-1
        mid = int(nlen/2)
        while end-start>2:
            if nums[mid]==mid:
                start = mid
                mid = int((end-start)/2+start)
            elif nums[mid]>mid:
                end = mid
                mid = int((end-start)/2+start)
            else:
                print("This will not happen!")
        # print(nums,start,end)
        for i in range(start,end):
            if nums[i+1]-nums[i]==1:
                continue
            else:
                if i==end:
                    return i-1
                return i+1


