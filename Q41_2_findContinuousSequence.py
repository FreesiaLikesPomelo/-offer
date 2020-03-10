'''
面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
限制：
1 <= target <= 10^5

执行用时 :284 ms, 在所有 Python3 提交中击败了40.24%的用户
内存消耗 :13.6 MB, 在所有 Python3 提交中击败了100.00%的用户
'''

# test cases:
# 1. target<3: return []
# 2. no qualified result: input 4, 8...
# 3. normal test: might contain more than one qualified list 

class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target<3:
            return []
        elif target==3:
            return [[1,2]]
        else:
            small = 1
            big = 2
            result = []
            while small<int((target+1)/2) and big>small: # 6:3, 9:5
                Sn = (small+big)*(big-small+1)/2
                if Sn==target:
                    temp = list(range(small,big+1))
                    result.append(temp)
                    small+=1
                elif Sn<target:
                    big+=1
                else: #Sn>target
                    small+=1
            return result
