# test cases:
# 1. n<=0 or m<0 : return None
# 2. n==1: return 1
# 3. function test
#    m = 1, delete it one by one.


#执行用时 :80 ms, 在所有 Python3 提交中击败了88.62%的用户
#内存消耗 :13.4 MB, 在所有 Python3 提交中击败了100.00%的用户

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<=0 or m<0:
            return None
        if n==1:
            return 0

        last = 0
        for i in range(2,n+1):
            last = (last+m)%i
            #print("f(",i,m,")",result)
        return last
        

'''
# 循环次数太多
# 超出时间限制 最后执行的输入： 70866, 116922
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<=0 or m<0:
            return None
        if n==1:
            return 1

        nums = list(range(n))
        idx = -1
        while len(nums)!=1:
            for i in range(m):
                if idx==len(nums)-1:
                    idx = 0
                else:
                    idx+=1
            nums.pop(idx)
            if idx==0:
                idx = len(nums)-1
            else:
                idx-=1
        return nums[0]
'''

'''
# to build the List, take to much time
# 超出时间限制 最后执行的输入： 70866, 116922
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<=0 or m<0:
            return None
        if n==1:
            return 1

        nums = list(range(n))
        head = ListNode(nums[0])
        start = head
        for i in range(1,n): # store them in a List
            temp = ListNode(nums[i])
            start.next = temp
            start = temp
            if i==n-1: # make it a circle
                # now start pointing to the tail node
                start.next = head

        listLen = n
        if m==1: # delete one by one
            while listLen!=1:
                temp = start.next.next
                start.next = temp
                listLen-=1
            return start.val
        else:
            while listLen!=1:
                for i in range(m-1):
                    start = start.next
                temp = start.next.next
                start.next = temp
                listLen-=1
            return start.val
'''

            


            

