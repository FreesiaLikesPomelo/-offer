# method :
# 1. quick Sort
# 2. rely on Partion(), half quick-sort
# 3. rely on tree storing the least k numbers

# test cases:
# 1. arr==[],return []
# 2. k<=0, return []
# 3. k > len(arr): return arr
# 4. function test

import random

class Solution:
    def swap(self, arr, i:int, j:int):
        if i==j:
            # print("now:",arr)
            return
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        # print("now:",arr)

    def Partion(self, arr)->int:
        '''
        rtype: int - small_idx, 
        this function is used to make sure, all numbers which are smaller than arr[small_idx] shift to the left of it, bigger numbers are on the right.
        '''
        if arr==[]:
            return 0,[]
        if len(arr)==1:
            return 0,arr
        
        end = len(arr)-1
        idx = random.randint(0,end)
        self.swap(arr, idx, end) # shift if to the end
        # print("randInt:", idx,"afterswap:",arr)

        small = -1
        for i in range(0,end):
            if arr[i]<arr[end]:
                small+=1
                if small!=i:
                    # print("parition swap: ", arr)
                    self.swap(arr, small, i)
        # print("Here, small=",small)
        small+=1
        self.swap(arr, small, end)
        return small,arr
	

    def quickSort(self, arr):
        if arr==[]:
            return []
        if len(arr)==1:
            return arr
        
        idx,arr = self.Partion(arr)
        # print("idx:",idx,"quicksort：",arr)
        if idx==0:
            # print("arr:", arr,)
            arr[idx+1:] = self.quickSort(arr[idx+1:])
        elif idx==len(arr)-1:
            # print("idx:",idx,"quicksort：",arr)
            arr[:idx] = self.quickSort(arr[:idx])
        else:
            arr[:idx] = self.quickSort(arr[:idx])
            arr[idx+1:] = self.quickSort(arr[idx+1:])
        return arr


    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if arr==[]:
            return []
        if k<=0:
            return []
        if k>len(arr):
            return arr
        
        # -- first method -- #
        arr.sort()
        return arr[:k]

        # -- second method -- #

        #self.quickSort(arr)
        #return arr[:k]

        # -- third method : half quick-sort -- #

            


