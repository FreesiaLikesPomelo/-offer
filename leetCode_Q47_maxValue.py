'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
示例 1:
输入: 
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 12
解释: 路径 1→3→5→2→1 可以拿到最多价值的礼物
提示：
0 < grid.length <= 200
0 < grid[0].length <= 200
'''

# test cases:
# 1. empty: return 0
# 2. [1,2,1]: can only move toward right direction
# 3. [[1,2],
#     [3,4],  return 1->3->5->6   --- greedy algorithm --- 
#     [5,6]] 
# 4. [[1,1,3],
#     [4,5,10],return 1->4->6->1->2  --- greedy algorithm --- 
#     [6,1,2]] return 1->4->5->10->2 # correct one; 
# dinamic program

# 执行用时 :44 ms, 在所有 Python3 提交中击败了99.30%的用户
# 内存消耗 :13.5 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if grid==[] or grid[0]==[]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        dp = [0]*cols
        # print(dp)
        for i in range(rows):
            for j in range(cols):
                if j==0:
                    dp[j]+=grid[i][j]
                else:
                    dp[j]= max(dp[j-1],dp[j])+grid[i][j]
        return dp.pop()
'''
# 执行用时 :52 ms, 在所有 Python3 提交中击败了90.59%的用户
# 内存消耗 :15.8 MB, 在所有 Python3 提交中击败了100.00%的用户
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        if grid==[] or grid[0]==[]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        dp = [[grid[0][0]]]

        # initiate the first column of dp
        # print(dp)
        for i in range(1,rows):
            dp.append([grid[i][0]+dp[i-1][0]]+[0]*(cols-1))
        # initiate the first row of dp
        for i in range(1,cols):
            dp[0].append(grid[0][i]+dp[0][i-1])
        # print(dp)
        # update dp
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        # print(dp)
        return dp[rows-1][cols-1]
'''
