'''
面试题53 - I. 在排序数组中查找数字 I
统计一个数字在排序数组中出现的次数。
示例 1:
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
示例 2:
输入: nums = [5,7,7,8,8,10], target = 6
输出: 0
限制：
0 <= 数组长度 <= 50000

执行用时 :32 ms, 在所有 Python3 提交中击败了96.80%的用户
内存消耗 :14.3 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# 二分查找
# test cases:
# 1.List==[] return 0
# 2. target is not in List; return 0
# 3. List contains only target 
# 4. only contain one target.

class Solution:
    def getFirst(self, nums:List[int], target: int, start: int, end: int)->int:
        # return the idx of the first target
        # if didn't find target in nums: return -1
        # if nums only contains contains one target: return -2
        #print("getFirst", nums, "start:",start,"end",end,nums[start:end+1])
        if end==start:
            if nums[start]==target:
                return start
            else: 
                return -1
        
        if end-start==1:#two numbers
            if nums[start]==target:
                return start
            elif nums[end]==target:
                return end
            else:
                return 0
        
        mid = int((end-start)/2)+start
        #print("mid",mid,"nums[",mid,"]",nums[mid])
        if nums[mid]==target:
            if mid==0:
                return mid
            if nums[mid-1]==target:
                return self.getFirst(nums,target,start,mid)
            else:
                if nums[mid+1]!=target:
                    return -2
                return mid
        elif nums[mid]<target:
            return self.getFirst(nums,target,mid+1,end)
        else:
            return self.getFirst(nums,target,start,mid-1)   
        
    def getLast(self,nums:List[int], target: int, start: int, end: int)->int:
        #print("getLast", nums, "start:",start,"end",end,nums[start:end+1])
        if start==end:
            if nums[start]==target:
                return start
            else:
                return -1
        
        if end-start==1:
            if nums[end]==target:
                return end
            elif nums[start]==target:
                return start
            else:
                return -1       
        
        mid = int((end-start)/2)+start
        #print("mid",mid,"nums[",mid,"]",nums[mid])
        if nums[mid]==target:
            if mid==len(nums)-1:# the last number
                return mid
            if nums[mid+1]==target:
                return self.getLast(nums,target,mid,end)
            else:
                return mid
        elif nums[mid]<target:
            return self.getLast(nums,target,mid+1,end)
        else:
            return self.getLast(nums,target,start,mid-1)


    def search(self, nums: List[int], target: int) -> int:
        #print("nums:",nums)
        if nums==[]:
            return 0
        
        if len(nums)==1:
            if target==nums[0]:
                return 1
            else:
                return 0

        first = self.getFirst(nums,target,0,len(nums)-1)
        #print("FirstKidx",first)
        if first==-1:
            return 0
        if first==-2:
            return 1
        last = self.getLast(nums,target,first,len(nums)-1)

        return last-first+1
