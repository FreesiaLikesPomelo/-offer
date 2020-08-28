# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 执行用时：40 ms, 在所有 Python3 提交中击败了91.95%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了46.93%的用户
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return 
        if head.next==None:
            return head
        if k<0:
            print(" k is negative number.")
            return
        if k==0:
            return head
        # get the length of the list
        temp = head
        n = 1
        while temp.next!=None:
            n+=1
            temp = temp.next
        # print("the length is :", n)
        realK = k%n
        if realK==0:
            return head
        # print("the real K is :", realK)
        temp.next = head # make it a ring list
        # find the second node from the tail:
        newHeadID = n - realK
        temp = head
        for i in range(0,newHeadID-1):
            temp = temp.next
        # print("the newHead is :",temp.val)
        pre = temp
        newHead = pre.next
        pre.next = None
        return newHead
'''
# 执行用时：48 ms, 在所有 Python3 提交中击败了53.62%的用户
# 内存消耗：13.7 MB, 在所有 Python3 提交中击败了65.26%的用户
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None:
            return 
        if head.next==None:
            return head
        if k<0:
            print(" k is negative number.")
            return
        if k==0:
            return head
        # get the length of the list
        temp = head
        n = 0
        while temp!=None:
            n+=1
            temp = temp.next
        #print("the length is :", n)
        realK = k%n
        if realK==0:
            return head
        #print("the real K is :", realK)
        # find the second node from the tail:
        newHeadID = n - realK
        temp = head
        for i in range(0,newHeadID-1):
            temp = temp.next
        #print("the newHead is :",temp.val)
        pre = temp
        newHead = pre.next
        pre.next = None
        temp = newHead
        while temp.next!=None:
            temp = temp.next
        tail = temp
        tail.next = head
        return newHead
'''
