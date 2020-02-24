'''
test cases:
1.empty list
2.only one row
3.only one column
4.only one column & one row
5.normal matrix--function test
'''

class Solution(object):
    def printOneCircle(self, matrix,row,column,start):
        """ 
        to print one circle of the matrix with four steps
        :type matrix: List[List[int]]
        :type row: int-- 
        :type column: int--
        :rtype: List[int]
        """
        result = []

        endx = row-1-start
        endy = column-1-start

        # step one -> print from left to right
        for i in range(start,endy+1):
            result.append(matrix[start][i])
            #print("step 1: ", matrix[start][i])
        
        # step two  print from top to button
        if start<endx:
            for i in range(start+1,endx+1):
                result.append(matrix[i][endy])
                #print("step 2: ", matrix[i][endy])
            
        # step three <- print from right to left
        if endx>start and endy>start: # (endx,endy-1)->(endx,start+1)
            i=endy-1
            #print("i = ", i)
            while i>=start:
                result.append(matrix[endx][i])
                #print("step 3: ",matrix[endx][i]," endy: ", endy, "start: ",start, "i: ",i)
                i-=1

        # step four  print from button to the top
        if endx-start>1 and endy>start:
            #print(matrix[start+1][start])
            i = endx-1
            while i>=start+1:
                result.append(matrix[i][start])
                #print("step 4: ", matrix[i][start])
                i-=1

        return result

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix==[]:
            return [] # empty list

        row = len(matrix)
        column = len(matrix[0])
        result = []
        
        if row==1:
            result.extend(matrix[0])
            return result # only one row or only one number
        elif column==1: # only one column 
            for i in range(row):
                result.extend(matrix[i])
            return result
            
            # flatten the list
        else:
            # each circle always starts from [x,x]
            start = 0
            result = []
            while row>2*start and column>2*start:
                result.extend(self.printOneCircle(matrix,row,column,start))
                start+=1
            return result

#a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
#s = Solution()
#r = s.spiralOrder(a)
#print(r)
