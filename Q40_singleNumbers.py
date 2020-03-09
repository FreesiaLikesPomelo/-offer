'''
面试题56 - I. 数组中数字出现的次数
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
示例 1：
输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：
输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
限制：
2 <= nums <= 10000

执行用时 :84 ms, 在所有 Python3 提交中击败了45.55%的用户
内存消耗 :14.4 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# using XOR
# a^a = 0; a^b^c^b = a^c

class Solution:
    def find1stBit(self,temp: int)-> int:
        # temp != 0
        idx = 0
        if temp&1==1:
            return idx
        while temp&1==0:
            temp = temp>>1
            idx+=1
        return idx
    
    def isBit1(self, num, idx)->bool:
        temp = num
        for i in range(idx):
            temp = temp>>1
        return temp&1

    def singleNumbers(self, nums: List[int]) -> List[int]:
        if len(nums)<2:
            return None
         
        if len(nums)==2:
            return nums

        temp = 0
        for i in nums:
            temp^=i

        idxOf1 = self.find1stBit(temp)
        # print("temp:",temp,"idxOf1",idxOf1)
        # seperate the List into two list.
        tempList0 = []
        tempList1 = []
        for i in nums:
            if self.isBit1(i,idxOf1)==1:
                tempList1.append(i)
            else:
                tempList0.append(i)
        # print("1st List:",tempList0,"2nd List:",tempList1)
       
        result = []
        temp = 0
        for i in tempList0:
            temp^=i
        result.append(temp)
        temp = 0
        for i in tempList1:
            temp^=i
        result.append(temp)
        return result

