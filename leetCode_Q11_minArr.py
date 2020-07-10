'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  
示例 1：
输入：[3,4,5,1,2]
输出：1
示例 2：
输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# [1 1 1 1 0]
# [2 2 2 2 2]
# [2 2 0 1 2] -> 也是旋转数组
# [5 1 2 3 4]

# 执行用时：40 ms, 在所有 Python3 提交中击败了77.59%的用户
# 内存消耗：13.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # numbers = [1,3,5]
        if len(numbers)==0:
            return None
        if len(numbers)==1:
            return numbers[0]
        
        l = 0
        r = len(numbers)-1
        idx = int((l+r)/2)
        flag = False
        #print("numbers:",l,":",numbers[l],"numbers:",r,":", numbers[r], "idx:",idx, numbers[l:r])
        while r-l>=2:
            if numbers[idx]>numbers[l]: # [3,4,5,1,2] [1,3,5] [1,3,5,1]
                if numbers[idx]>numbers[r]:
                    l = idx
                    idx = int((l+r)/2)
                else:
                    r = idx
                    idx = int((l+r)/2)
            elif numbers[idx]<numbers[l]: # [5 1 2 3 4]
                r = idx
                idx = int((l+r)/2)
            else: # [2 1 2 2 2], [2 2 2 1 2]
                l = l+1
                idx = int((l+r)/2)
            #print("numbers:",l,":",numbers[l],"numbers:",r,":", numbers[r], "idx:",idx, numbers[l:r])
        #print("numbers:",l,":",numbers[l],"numbers:",r,":", numbers[r], "idx:",idx, numbers[l:r])
        if numbers[l]>numbers[r]:
            return numbers[r]
        elif numbers[l]<numbers[r]:
            return numbers[l]
        else:
            return numbers[l]

'''
# 执行用时：48 ms, 在所有 Python3 提交中击败了28.18%的用户
# 内存消耗：14 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        if len(numbers)==0:
            return None
        if len(numbers)==1:
            return numbers[0]

        # scan from the beginning, comparing two numbers close to each other, the first smaller latter is the answer
        for i in range(len(numbers)-1):
            if numbers[i+1]<numbers[i]:
                return numbers[i+1]
            if i==len(numbers)-2:
                # can't find the answer untill the last one
                return numbers[0]
'''
