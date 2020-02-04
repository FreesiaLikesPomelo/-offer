# -*- coding:utf-8 -*-
# partially ordered, considering binary search
'''
test case
1,normal cases:{3,4,5,1,2}
2,normal cases with same normals:{3,4,5,1,2,3}
3,rotate 0 numbers:{1,2,3,4,5}
4,that start, end, middle elements are the same:{1,1,1,1,0,1},{1,0,1,1,1}
'''
# passed on Leetcode, but not passed on nowCoder >.<

class Solution(object):
    def findMin(self, rotateArray):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(rotateArray)==0:
            return 0
        end = len(rotateArray)-1
        middle = len(rotateArray)/2
        start = 0
        if rotateArray[start]<rotateArray[end]:
            return rotateArray[start]
        elif rotateArray[start]>rotateArray[end]:
            # Binary Search
            #print("Binary Search 1")
            while(end-start>1):# 
                if rotateArray[middle]>rotateArray[start]:
                    return self.findMin(rotateArray[middle:])
                else:
                    return self.findMin(rotateArray[:middle+1])
            return rotateArray[end]
        else: # rotateArray[start]=rotateArray[end]
            if rotateArray[middle] == rotateArray[start]:
                # Sequential Search
                smallest = rotateArray[0]
                for i in range(end+1):
					if rotateArray[i]<smallest:
						smallest = rotateArray[i]
                return smallest
            else:
                # Binary Search
                while(end-start>1):# 
                    if rotateArray[middle]>rotateArray[start]:
                        return self.findMin(rotateArray[middle:])
                    else:
                        return self.findMin(rotateArray[:middle+1])
                return rotateArray[end]
              
