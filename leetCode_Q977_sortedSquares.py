# negative elements [-1,0,1] -> [0,1,1]
# same elements [-2,-2,0,2] -> [0,2,2,2]

"""
977. 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
"""

def square(num):
    return num*num

"""
执行用时：52 ms, 在所有 Python3 提交中击败了99.73%的用户
内存消耗：16.5 MB, 在所有 Python3 提交中击败了5.01%的用户

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums==[]:
            return
        elif len(nums)==1:
            return [nums[0]*nums[0]]
        else:
            absNums = list(map(abs,nums))
            # print(absNums)
            absNums.sort()
            # print(absNums)
            result = list(map(square,absNums))
            # print(result)
            return result
"""



"""
执行用时：68 ms, 在所有 Python3 提交中击败了98.08%的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了5.01%的用户
"""
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums==[]:
            return
        elif len(nums)==1:
            return [nums[0]*nums[0]]
        else:
            neg = -1
            for i in range(len(nums)):
                if nums[i]<0:
                    neg = i
            
            if neg==-1:
                return list(map(square,nums))
            elif neg==len(nums)-1:
                ans = list(map(square,nums))
                ans.sort()
                return ans
            else:
                num1 = list(map(square,nums[0:neg+1]))
                num2 = list(map(square,nums[neg+1:]))
                idxl,idxr = len(num1)-1,0
                ans = []
                while idxl>=0 and idxr<len(num2):
                    if num2[idxr]<num1[idxl]:
                        ans.append(num2[idxr])   
                        idxr+=1
                    else:
                        ans.append(num1[idxl])
                        idxl-=1
                if idxl<0:
                    while idxr<len(num2):
                        ans.append(num2[idxr])
                        idxr+=1
                else:
                    while idxl>=0:
                        ans.append(num1[idxl])
                        idxl-=1
                return ans
                               
                

            
