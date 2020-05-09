'''
面试题04. 二维数组中的查找
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。

限制：
0 <= n <= 1000
0 <= m <= 1000
'''

# search from the top-right corner
# test cases:
# [[]]->return False
# [[3]]->

# 执行用时 :44 ms, 在所有 Python3 提交中击败了84.60%的用户
# 内存消耗 :17.9 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        #matrix=[[-5]]
        #target = -5
        if len(matrix)==0:
            return False
        row = len(matrix) # start from 0 to row-1
        column = len(matrix[0]) # start from column-1 to 0

        i=0
        j=column-1
        while i<=row-1 and j>=0:
            if matrix[i][j]==target:
                #print("i:",i,"j:",j,"Matrix_data:",matrix[i][j],"=target:",target)
                return True
            elif matrix[i][j]<target:
                #print("i:",i,"j:",j,"Matrix_data:",matrix[i][j],"<target:",target)
                i+=1
            else:
                #print("i:",i,"j:",j,"Matrix_data:",matrix[i][j],">target:",target)
                j-=1
        return False

