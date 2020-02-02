# -*- coding:utf-8 -*-
# 二维数组中的查找
# searching in 2-demensional matrix

#this program is to find whether the given number is in the mxn matrix,
#we can start from the top right-hand corner,array[0][col-1]
#if target is not in array, then the end-point will be array[row-1][0]

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        r = 0
        c = col-1
        while c>=0 and r<row:
            if(array[r][c]==target):
                return 'true'
            elif(array[r][c]>target):
                c-=1
            else:
                r+=1
        return 'false'
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(raw_input()))
        #L = [7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]]
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break

'''
通过率35.29% 20200131
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        row = len(array)
        col = len(array[0])
        r = 0
        c = col-1
        flag='false'
        while(c>=0 & r<row):
            if(array[r][c]==target):
                flag='true'
                break
            elif(array[r][c]>target):
                c-=1
            else:
                r+=1
        return flag

# 以下为牛客网测试用例  	
while True:
    try:
        S=Solution()
        # 字符串转为list
        L=list(eval(raw_input()))
        #L = [7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]]
        array=L[1]
        target=L[0]
        print(S.Find(target, array))
    except:
        break
'''
'''
# 以下为运行测试例
try:
	S=Solution()
    # 字符串转为list
    #L=list(eval(raw_input()))
	L=[7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]]
	array=L[1]
	target=L[0]
	print(S.Find(target, array))
except:
	print("Break")
'''
